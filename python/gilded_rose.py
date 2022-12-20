# -*- coding: utf-8 -*-
from __future__ import annotations
from typing import Type
"""
- Use OOP approach
- Encapsulate item state in wrapper.
"""
class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def _classify_special_items(self, items):
        special_items = SpecialItemTypes()
        special_items.add_item_type('Aged Brie', AgedBrie)
        special_items.add_item_type("Sulfuras, Hand of Ragnaros", Sulfuras)
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
        self._item = item

    def _item_quality_change_rate(self):
        if self._item.sell_in > 0:
            return -1
        else:
            return -2

    def _item_sell_in_change_rate(self):
        return -1

    def _update_sell_in(self):
        self._item.sell_in += self._item_sell_in_change_rate()

    def _ensure_quality_within_bounds(self):
        if self._item.quality > 50:
            self._item.quality = 50
        if self._item.quality < 0:
            self._item.quality = 0

    def _update_quality(self):
        self._item += self._item_quality_change_rate()
        self._ensure_quality_within_bounds()

    def update(self):
        self._update_sell_in()
        self._update_quality()


class AgedBrie(BasicItem):

    def _item_quality_change_rate(self):
        if self._item.sell_in > 0:
            return 1
        else:
            return 2

class Sulfuras(BasicItem):

    def _item_quality_change_rate(self):
        return 0

    def _item_sell_in_change_rate(self):
        return 0


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