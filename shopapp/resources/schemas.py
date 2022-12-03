from __future__ import annotations
from enum import Enum, auto

from marshmallow import Schema, fields


print(f"Importing schemas: {__name__}")


class PutActionEnum(Enum):
    CREATE_LIST = auto(),
    ADD_ITEM = auto()
    pass


class PutActionSchema(Schema):
    action = fields.Enum(PutActionEnum, required=True)
    payload = fields.Dict(required=True)


class AddItemSchema(Schema):
    item_name = fields.Str(required=True)
    item_qty = fields.Int(required=False)


class CreateListSchema(Schema):
    list_name = fields.Str(required=True)
