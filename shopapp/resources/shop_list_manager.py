from __future__ import annotations
from typing import Dict
from .shopping_list import ShoppingList
from flask import abort

print(f"Importing: {__name__}")


class ShopListManager():

    def __init__(self) -> None:
        super().__init__()
        self.lists = {}
        pass

    # @TODO

    def addList(self, payload):
        name = payload["list_name"]
        errors = []

        if name in self.lists:
            errors.append(f"List {name} already exists")
        else:
            print("Adding list", name)
            slist = ShoppingList(name)
            self.lists[name] = slist
            pass

        print(str(self.lists))

        return errors
        pass

    def addItem(self, list, item):

        pass

    pass
