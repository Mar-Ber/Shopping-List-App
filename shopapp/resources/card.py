from __future__ import annotations
from typing import Dict, List
import barcode
from barcode.writer import ImageWriter
import matplotlib.pyplot as plt
import PIL.Image
from .schemas import CardFields, CommonFields
import base64
import io


class Card():
    def __init__(self, number, name, store, format) -> None:
        self.number_ = number
        self.name_ = name
        self.store_ = store
        self.format_ = format

        EAN = barcode.get_barcode_class(self.format_)
        validated_ean = EAN(str(self.number_))
        pass

    def getInfo(self):
        ret_dict = {
            CardFields.STORE: self.store_,
            CardFields.NUMBER: self.number_,
            CardFields.FORMAT: self.format_,
            CommonFields.NAME: self.name_
        }
        return ret_dict
        pass

    def getBarcode(self):
        ret_dict = {}
        ret_dict[CardFields.BARCODE] = self.generateBarcode()
        return ret_dict
        pass

    def generateBarcode(self):
        EAN = barcode.get_barcode_class(self.format_)
        writer_ = ImageWriter(mode="L")
        writer_.set_options({'text_distance': 0.0, "center_text": True})

        card_ean = EAN(str(self.number_), writer=writer_)
        barcode_text = f"{self.number_}\n{self.store_}"

        if self.name_:
            barcode_text += f" \n{self.name_}"

        barcode_image: PIL.Image.Image
        barcode_image = card_ean.render(
            {'text_distance': 3.0, "center_text": True}, text=barcode_text)
        barcode_image.convert("L")

        width, height = barcode_image.size
        bio = io.BytesIO()
        barcode_image.save(bio, format="PNG")
        barcode_image_b64 = base64.b64encode(bio.getvalue()).decode("utf-8")
        barcode_data = {
            self.name_:
                {
                    CardFields.IMAGE_WIDTH: width,
                    CardFields.IMAGE_HEIGHT: height,
                    CardFields.IMAGE_PNG_B64: barcode_image_b64
                }
        }
        return barcode_data
        pass
    pass
