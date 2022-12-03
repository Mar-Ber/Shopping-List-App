from __future__ import annotations

from .schemas import AddItemSchema, PutActionSchema, PutActionEnum, CreateListSchema, Schema
from .shop_list_manager import ShopListManager

from flask import abort, redirect, url_for
from flask_restful import Resource, Api
from flask import Flask, request, abort

import flask


print(f"Importing ItemManagerAPI: {__name__}")


manager_ = ShopListManager()


class ShopListManagerAPI(Resource):

    def __init__(self) -> None:
        super().__init__()

        self.__name__ = "shopapp"
        pass

    def put(self):
        #print("Request json:", request.json)
        #errors = self.action_schema.validate(request.json)
        try:
            t = PutActionSchema().loads(request.data)
            action = t["action"]
            payload = t["payload"]
            schema: Schema
            schema, callback = self.validatePutAction(action)

            if schema is None:
                errors = "Action not valid"
            else:
                errors = schema.validate(payload)
                pass

            if errors:
                self.badRequest(errors)
                pass

            callback_errors = callback(payload)
            if callback_errors:
                self.badRequest(callback_errors)
                pass

            return str(t)
            pass

        except Exception as e:
            print(e)
            self.badRequest(e)
            pass

        return "Unhandled case"
        pass

    def validatePutAction(self, action):
        schema = None
        callback = None

        if action == PutActionEnum.ADD_ITEM:
            schema = AddItemSchema()

        if action == PutActionEnum.CREATE_LIST:
            schema = CreateListSchema()
            callback = manager_.addList

        return (schema, callback)
        pass

    def get(self):
        return "Test get"

    def badRequest(self, e):
        abort(400, str(e))
        pass

    pass
