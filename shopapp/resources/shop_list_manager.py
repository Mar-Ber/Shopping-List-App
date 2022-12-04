from __future__ import annotations
from typing import Dict
from .shopping_list import ShoppingList
from .item import Item
from .schemas import CommonFields

print(f"Importing: {__name__}")


class ShopListManager():

    def __init__(self) -> None:
        super().__init__()
        self.lists = {}
        pass

    # @TODO

    def addList(self, payload):
        name = payload[CommonFields.LIST_NAME]
        ret_dict = {CommonFields.ERRORS: []}

        if name in self.lists:
            ret_dict[CommonFields.ERRORS].append(f"List {name} already exists")
        else:
            print("Adding list", name)
            slist = ShoppingList(name)
            self.lists[name] = slist
            pass
        print(str(self.lists))

        return ret_dict
        pass

    def addItem(self, payload: Dict):
        ret_dict = {CommonFields.ERRORS: []}

        name = payload[CommonFields.NAME]
        target_list = payload[CommonFields.LIST_NAME]
        qty = payload.get("qty")
        price = payload.get("price")

        item = Item(name, qty, price)
        target_list: ShoppingList = self.lists.get(target_list)

        errors = None
        if target_list is None:
            ret_dict[CommonFields.ERRORS].append("Target list doesn't exist")
        else:
            errors = target_list.addItem(item)
            target_list.printAllItems()
            pass

        if errors:
            ret_dict[CommonFields.ERRORS].append(errors)

        return ret_dict
        pass

    pass
