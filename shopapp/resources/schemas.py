from __future__ import annotations

from marshmallow import Schema, fields

print(f"Importing schemas: {__name__}")
class AddItemSchema(Schema):
    item_name = fields.Str(required = True)
    item_qty = fields.Int(required = False)