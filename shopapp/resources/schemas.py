from __future__ import annotations
from enum import Enum, auto
import types

from marshmallow import Schema, fields


print(f"Importing schemas: {__name__}")


class PutActionEnum(Enum):
    CREATE_LIST = auto()
    ADD_ITEM = auto()
    ADD_CARD = auto()
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

class ItemFields(str, Enum):
    PRICE = "price"
    QTY = "qty"
    pass

class CardFields(str, Enum):
    NUMBER = "number"
    STORE = "store"
    FORMAT = "format"
    pass

class CardFormatsEnum(str, Enum):
    EAN8 = "ean8"
    EAN13 = "ean13"
    pass

class PutActionSchema(Schema):
    pass

class GetActionSchema(Schema):
    pass

class AddItemSchema(Schema):
    pass

class CreateListSchema(Schema):
    pass

class AddCardSchema(Schema):
    pass

PutActionSchema = type('PutActionSchema', (Schema,), {
    CommonFields.ACTION.value: fields.Enum(PutActionEnum, required=True),
    CommonFields.PAYLOAD.value: fields.Dict(required=True)
})

GetActionSchema = type('GetActionSchema', (Schema,), {
    CommonFields.ACTION.value: fields.Enum(GetActionEnum, required=True),
    CommonFields.PAYLOAD.value: fields.Dict(required=True)
})

AddItemSchema = type('AddItemSchema', (Schema,), {
    CommonFields.NAME.value: fields.Str(required=True),
    CommonFields.LIST_NAME.value: fields.Str(required=True),
    #NOT REQUIRED
    ItemFields.QTY.value: fields.Int(required=False),
    ItemFields.PRICE.value: fields.Float(required=False)
})

CreateListSchema = type("CreateListSchema", (Schema,), {
    CommonFields.LIST_NAME.value: fields.Str(required=True)
})

AddCardSchema = type("AddCardSchema", (Schema,), {
    CardFields.NUMBER.value: fields.Int(required=True),
    CardFields.STORE.value: fields.Str(required=True),
    CardFields.FORMAT.value: fields.Enum(CardFormatsEnum, required=True),
    #NOT REQUIRED
    CommonFields.NAME.value: fields.Str(required=False)
})

