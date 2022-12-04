from __future__ import annotations
from enum import Enum, auto

from marshmallow import Schema, fields


print(f"Importing schemas: {__name__}")


class PutActionEnum(Enum):
    CREATE_LIST = auto(),
    ADD_ITEM = auto()
    pass


class GetActionEnum(Enum):
    LISTS = auto()
    ITEMS_IN = auto()
    pass


class CommonFields(str, Enum):
    NAME = "name"
    ERRORS = "errors"
    LIST_NAME = "list_name"
    ACTION = "action"
    PAYLOAD = "payload"
    pass


class PutActionSchema(Schema):
    action = fields.Enum(PutActionEnum, required=True)
    payload = fields.Dict(required=True)


class GetActionSchema(Schema):
    action = fields.Enum(GetActionEnum, required=True)
    payload = fields.Dict(required=True)


class AddItemSchema(Schema):
    name = fields.Str(required=True)
    list_name = fields.Str(required=True)

    qty = fields.Int(required=False)
    price = fields.Float(required=False)


class CreateListSchema(Schema):
    list_name = fields.Str(required=True)
