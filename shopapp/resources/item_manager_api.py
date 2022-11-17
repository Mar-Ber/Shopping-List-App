from __future__ import annotations
print(f"Importing ItemManagerAPI: {__name__}")

import flask
from flask import Flask, request, abort
from flask_restful import Resource, Api
from flask import abort, redirect, url_for

from .item_manager import ItemManager
from .schemas import AddItemSchema

class ItemManagerAPI(Resource):

    def __init__(self) -> None:
        super().__init__()
        self.manager_  = ItemManager()
        self.add_item_schema = AddItemSchema()
        pass

    def put(self):
        errors = self.add_item_schema.validate(request.args)
        #print(self.add_item_schema.load(request.args))
        if errors:
            abort(400, str(errors))

        return 'ok'
        pass

    def get(self):
        return "Test get"

    pass