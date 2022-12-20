# -*- coding: utf-8 -*-
from __future__ import annotations
from typing import Type
"""
- Use OOP approach
- Encapsulate item state in wrapper.
"""
class GildedRose(object):

    def __init__(self, items):
        self.items = self._classify_special_items(items)

    def _classify_special_items(self, items):
        special_items = SpecialItemTypes()
        special_items.add_item_type('Aged Brie', AgedBrie)
        return [special_items.classify_item(item) for item in items]

    def update_quality(self):
        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.quality = item.quality - 1
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class BasicItem(Item):
    def __init__(self, item: Item):
        super().__init__(item.name, item.sell_in, item.quality)

    def update(self):
        self._reduce_quality()
        self._reduce_sell_in()

    def _reduce_quality(self):
        if self.sell_in > 0:
            self.quality -= 1
        else:
            self.quality -= 2

    def _reduce_sell_in(self):
        self.sell_in -= 1



class AgedBrie(BasicItem):
   pass



class SpecialItemTypes:
    item_types: dict[str, Item]

    def __init__(self):
        self.item_types = {}

    def add_item_type(self, item_name :str, item_class: Type[Item]):
        self.item_types[item_name] = item_class

    def classify_item(self, item: Item):
        if item.name in self.item_types.keys():
            return self.item_types[item.name](item)
        else:
            return BasicItem(item)