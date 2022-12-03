from __future__ import annotations
from typing import Dict
from .shopping_list import ShoppingList

print(f"Importing: {__name__}")


class ShopListManager():

    def __init__(self) -> None:
        super().__init__()
        self.lists = Dict[str, ShoppingList]
        pass

    # @TODO

    def addList(self, payload):
        name = payload["list_name"]
        print("Adding list", name)

        if name in self.lists:
            print("Cannot add list with same name")
        else:
            self.lists[name] = ShoppingList(name)
            pass
        print(self.lists)

        pass

    def addItem(self, list, item):

        pass

    pass
