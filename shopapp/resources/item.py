from __future__ import annotations
from typing import Dict, List


class Item():
    def __init__(self, name, qty, price) -> None:
        self.name_ = name
        self.qty_ = qty
        self.price_ = price
        pass

    def __repr__(self) -> str:
        repr_str = f"""
        ### ITEM ###
        Name: {self.name_}
        Qty: {self.qty_}
        Price: {self.price_}
        ############"""

        return repr_str
        pass
    pass
