from __future__ import annotations
from typing import Dict, List


class Card():
    def __init__(self, number, name, store, format) -> None:
        self.number_ = number
        self.name_ = name
        self.store_ = store
        self.format_ = format
        pass

    def generateBarcode(self):
        pass
    pass
