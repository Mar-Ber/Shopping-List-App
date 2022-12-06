from __future__ import annotations
from enum import Enum, auto
import types

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


class CardFields(str, Enum):
    pass


class PutActionSchema(Schema):
    pass


PutActionSchema = type('PutActionSchema', (Schema,), {
    CommonFields.ACTION.value: fields.Enum(PutActionEnum, required=True),
    CommonFields.PAYLOAD.value: fields.Dict(required=True)
})


class GetActionSchema(Schema):
    action = fields.Enum(GetActionEnum, required=True)
    payload = fields.Dict(required=True)
    pass


class AddItemSchema(Schema):
    name = fields.Str(required=True)
    list_name = fields.Str(required=True)

    qty = fields.Int(required=False)
    price = fields.Float(required=False)
    pass


class CreateListSchema(Schema):
    list_name = fields.Str(required=True)
    pass


class CreateCardSchema(Schema):
    pass
