from __future__ import annotations
from typing import Dict, List
from .item import Item


class ShoppingList():
    def __init__(self, name) -> None:
        self.name_ = name
        self.items = []
        pass

    def addItem(self, item: Item):
        self.items.append(item)
        errors = None
        return errors
        pass

    def printAllItems(self):
        item: Item
        print(f"### ITEMS IN LIST : {self.name_} ###")
        for item in self.items:
            print(item)
    pass
