from __future__ import annotations

from marshmallow import Schema

from .schemas import PutActionEnum, GetActionEnum
from .schemas import PutActionSchema, GetActionSchema
from .schemas import AddItemSchema, CreateListSchema, AddCardSchema
from .schemas import GetCardSchema


from .shop_list_manager import ShopListManager
from .schemas import CommonFields
from flask import abort, redirect, url_for
from flask_restful import Resource, Api
from flask import Flask, request, abort

import flask


print(f"Importing ItemManagerAPI: {__name__}")


manager_ = ShopListManager()


class ShopListManagerAPI(Resource):

    def __init__(self) -> None:
        super().__init__()
        pass

    def validateRequest(self, schema: Schema, actionValidator: callable):
        try:
            t = schema.loads(request.data)
            action = t[CommonFields.ACTION]
            print("ACTION TYPE:", type(action))
            payload = t[CommonFields.PAYLOAD]
            print(t)
            print(payload)
            schema: Schema
            schema, callback = actionValidator(action)

            errors = None
            if schema is None:
                errors = "Action not valid"

            if callback is None:
                errors = "Action callback not assigned"

            if errors is None:
                errors = schema.validate(payload)
                pass

            if errors:
                ret_errors = {CommonFields.ERRORS: errors}
                self.badRequest(ret_errors)  # LEAVING
                pass

            ret_dict = callback(payload)
            if ret_dict is not None:
                ret_errors = ret_dict.get(CommonFields.ERRORS)

            if ret_errors:
                self.badRequest(ret_errors)  # LEAVING
                pass

            return ret_dict
            pass

        except Exception as e:
            ret_errors = {CommonFields.ERRORS: str(e)}
            print("Caught exception", str(e))
            self.badRequest(ret_errors)  # LEAVING
            pass

        return "Unhandled case"
        pass

    def put(self):
        ret = self.validateRequest(PutActionSchema(), self.validatePutAction)
        return ret
        pass

    def get(self):
        ret = self.validateRequest(GetActionSchema(), self.validateGetAction)
        return ret
        pass

    def validatePutAction(self, action):
        schema = None
        callback = None

        if action is None:
            pass

        elif action == PutActionEnum.ADD_ITEM:
            schema = AddItemSchema()
            callback = manager_.addItem

        elif action == PutActionEnum.CREATE_LIST:
            schema = CreateListSchema()
            callback = manager_.addList

        elif action == PutActionEnum.ADD_CARD:
            schema = AddCardSchema()
            callback = manager_.addCard

        return (schema, callback)
        pass

    def validateGetAction(self, action):
        schema = None
        callback = None

        if action is None:
            pass

        elif action == GetActionEnum.LISTS:
            schema = None

        elif action == GetActionEnum.ITEMS:
            schema = None

        elif action == GetActionEnum.CARD_DATA:
            schema = GetCardSchema()
            callback = manager_.getCardData

        return (schema, callback)
        pass

    def badRequest(self, e):
        abort(400, str(e))
        pass

    pass
