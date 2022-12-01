from __future__ import annotations
# -*- coding: utf-8 -*-

SPECIAL_ITEMS = [
    "Aged Brie",
    "Sulfuras, Hand of Ragnaros",
    "Backstage passes to a TAFKAL80ETC concert"
]

class GildedRose(object):

    def __init__(self, items: list[Item]):
        self.items = []
        for item in items:
            if item.name not in SPECIAL_ITEMS:
                self.items.append(ItemAger(item))
            else:
                self.items.append(item)

    def update_quality(self):
        for item in self.items:
            if isinstance(item, ItemAger):
                item.update_quality()
            else:
                self._update_quality_legacy(item)

    def _update_quality_legacy(self, item: Item):
        '''Legacy method to update item quality, still used for more complex items while we refactor'''
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



class ItemAger:

    def __init__(self, item: Item):
        self.item = item
        self.age_rate = -1

    def update_quality(self):
        self.item.sell_in -= 1
        if self.item.quality > 0:
            self.item.quality += self.age_rate
        if self.item.sell_in <= 0:
            self.age_rate = -2




class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

