# -*- coding: utf-8 -*-
from __future__ import annotations
from typing import Type
"""
- Use OOP approach
- Encapsulate item state in wrapper.
"""

class GildedRose(object):

    def __init__(self, items):

        self.inventory = Inventory()
        self.inventory.add_special_item_type('Aged Brie', AgedBrie)
        self.inventory.add_special_item_type("Sulfuras, Hand of Ragnaros", Sulfuras)
        self.inventory.add_special_item_type("Backstage passes to a TAFKAL80ETC concert", BackStagePass)

        self.inventory.add_items(items)

    def update_quality(self):
        self.inventory.update_items()


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

    def _item_sell_in_change_rate(self):
        return -1

    def _item_quality_change_rate(self):
        if self._item.sell_in > 0:
            return -1
        else:
            return -2

    def _ensure_quality_within_bounds(self):
        if self._item.quality > 50:
            self._item.quality = 50
        if self._item.quality < 0:
            self._item.quality = 0

    def _update_sell_in(self):
        self._item.sell_in += self._item_sell_in_change_rate()

    def _update_quality(self):
        self._item.quality += self._item_quality_change_rate()
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

class BackStagePass(BasicItem):

    def _item_quality_change_rate(self):
        if self._item.sell_in < 0:
            return -(self._item.quality)
        if self._item.sell_in < 5:
            return 3
        if self._item.sell_in < 10:
            return 2
        return 1





class SpecialItemTypes:
    item_types: dict[str, Item]

    def __init__(self):
        self.item_types = {}

    def add(self, item_name :str, item_class: Type[Item]):
        self.item_types[item_name] = item_class

    def is_special_item(self, item: Item):
        return item.name in self.item_types.keys()

    def get_special_item_type(self, item: Item):
        return self.item_types[item.name]




class Inventory:
    items: list[BasicItem]

    def __init__(self):
        self.special_item_types = SpecialItemTypes()
        self.items = []

    def add_special_item_type(self, item_name :str, item_class: Type[Item]):
        self.special_item_types.add(item_name, item_class)

    def add_item(self, item: Item):
        if self.special_item_types.is_special_item(item):
                item_type = self.special_item_types.get_special_item_type(item)
                self.items.append(item_type(item))
        else:
            self.items.append(BasicItem(item))

    def add_items(self, items: list[Item]):
        for item in items:
            self.add_item(item)

    def update_items(self):
        for item in self.items:
            item.update()
