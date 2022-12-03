from __future__ import annotations
from typing import Dict, List
from .item import Item


class ShoppingList():
    def __init__(self, name) -> None:
        self.name_ = name
        self.items = List[Item]
        pass

    pass
