from __future__ import annotations
from ast import List
from typing import Dict
from .shopping_list import ShoppingList
from .item import Item
from .card import Card
from .schemas import CommonFields, CardFields, ItemFields, CardFormatsEnum

print(f"Importing: {__name__}")


class ShopListManager():

    def __init__(self) -> None:
        super().__init__()
        self.lists_ = {}
        self.cards_ = {}
        pass

    # @TODO

    def addList(self, payload):
        name = payload[CommonFields.LIST_NAME]
        ret_dict = {CommonFields.ERRORS: []}

        if name in self.lists_:
            ret_dict[CommonFields.ERRORS].append(f"List {name} already exists")
        else:
            print("Adding list", name)
            slist = ShoppingList(name)
            self.lists_[name] = slist
            pass
        print(str(self.lists_))

        return ret_dict
        pass

    def addItem(self, payload: Dict):
        ret_dict = {CommonFields.ERRORS: []}

        name = payload[CommonFields.NAME]
        target_list = payload[CommonFields.LIST_NAME]
        qty = payload.get(ItemFields.QTY)
        price = payload.get(ItemFields.PRICE)

        item = Item(name, qty, price)
        target_list: ShoppingList = self.lists_.get(target_list)

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

    def addCard(self, payload: Dict):
        ret_dict = {CommonFields.ERRORS: []}

        number = payload[CardFields.NUMBER]
        store = payload[CardFields.STORE]
        format = CardFormatsEnum[payload[CardFields.FORMAT]]
        name = payload.get(CommonFields.NAME)

        if store not in self.cards_.keys():
            self.cards_[store] = []

        try:
            card = Card(number=number, store=store, name=name, format=format)
            self.cards_[store].append(card)

        except Exception as e:
            ret_dict[CommonFields.ERRORS].append(str(e))
            print(ret_dict)
            pass

        return ret_dict
        pass

    def getCardData(self, payload: Dict):
        ret_dict = {CardFields.CARDS: []}

        number = payload.get(CardFields.NUMBER)
        store = payload.get(CardFields.STORE)
        name = payload.get(CommonFields.NAME)

        prelim_cards = []

        if store is not None:
            prelim_cards = self.cards_.get(store)
        else:
            for store in self.cards_:
                for card in self.cards_[store]:
                    prelim_cards.append(card)
                pass
            pass

        if prelim_cards is None:
            return ret_dict

        card: Card
        ret_cards = []
        for card in prelim_cards:
            info = card.getInfo()

            accept_name = name is None or (info[CommonFields.NAME] == name)
            accept_number = number is None or (
                info[CardFields.NUMBER] == number)

            accepted = accept_name and accept_number

            if accepted:
                ret_cards.append(card)
            pass

        for card in ret_cards:
            ret_dict[CardFields.CARDS].append(card.getInfo())
        return ret_dict
    pass

    def getCardBarcodes(self, payload):
        ret_dict = {CardFields.CARDS: []}

        number = payload.get(CardFields.NUMBER)
        store = payload.get(CardFields.STORE)
        name = payload.get(CommonFields.NAME)

        prelim_cards = []

        if store is not None:
            prelim_cards = self.cards_.get(store)
        else:
            for store in self.cards_:
                for card in self.cards_[store]:
                    prelim_cards.append(card)
                pass
            pass

        if prelim_cards is None:
            return ret_dict

        card: Card
        ret_cards = []
        for card in prelim_cards:
            info = card.getInfo()

            accept_name = name is None or (info[CommonFields.NAME] == name)
            accept_number = number is None or (
                info[CardFields.NUMBER] == number)

            accepted = accept_name and accept_number

            if accepted:
                ret_cards.append(card)
            pass

        for card in ret_cards:
            ret_dict[CardFields.CARDS].append(card.getBarcode())
        return ret_dict
        pass

    def getLists(self, payload):
        ret_dict = {CommonFields.ERRORS: [], ItemFields.ITEMS: []}
        if not self.lists_:
            ret_dict[CommonFields.ERRORS].append("No lists to display")
        else:
            ret_dict[CommonFields.LIST_NAME] = list(self.lists_.keys())
        return ret_dict
        pass

    def getItems(self, payload:Dict):
        ret_dict = {CommonFields.ERRORS: []}

        list_name = payload.get(CommonFields.LIST_NAME)

        items = []
        if list_name:

            if list_name not in self.lists_:
                ret_dict[CommonFields.ERRORS].append(f"No list named {list_name}")
                return ret_dict

            for item in self.lists_[list_name].items:
                items.append(item.name_)

            ret_dict[CommonFields.LIST_NAME] = list_name
        else:
            for list in self.lists_:
                self.lists_:List(ShoppingList)
                item: Item
                for item in self.lists_[list].items:
                    items.append(item.name_)

        ret_dict[ItemFields.ITEMS] = items

        if not items:
            ret_dict[CommonFields.ERRORS].append("No items to display")

        return ret_dict
        pass
