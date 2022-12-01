from __future__ import annotations
from abc import ABC, abstractmethod
# -*- coding: utf-8 -*-

SPECIAL_ITEMS = [
    "Backstage passes to a TAFKAL80ETC concert",
]


class ItemAger(ABC):
    @abstractmethod
    def update_quality(self) -> None:
        ...

class BasicItemAger(ItemAger):

    def __init__(self, item: Item):
        self.item = item

    def update_quality(self):
        ''' Update quality of item'''
        self.item.sell_in -= 1
        if self.item.sell_in >= 0:
            self.item.quality -= 1
        else:
            self.item.quality -= 2

        if self.item.quality < 0:
            self.item.quality = 0

class AgedBrieAger(ItemAger):
    def __init__(self, item: Item):
         self.item = item

    def update_quality(self):
        self.item.sell_in -= 1
        if self.item.sell_in >= 0:
            self.item.quality += 1
        else:
            self.item.quality +=2

        if self.item.quality > 50:
            self.item.quality = 50


class SulfurasAger(ItemAger):
    def __init__(self, item: Item):
         self.item = item

    def update_quality(self):
        pass



AGERS = {
    'Aged Brie': AgedBrieAger,
    'Sulfuras, Hand of Ragnaros': SulfurasAger
}

class GildedRose(object):

    def __init__(self, items: list[Item]):
        self.items = []
        for item in items:
            if item.name in SPECIAL_ITEMS:
                self.items.append(item)
            else:
                try:
                    ager = AGERS[item.name](item)
                except KeyError:
                    ager = BasicItemAger(item)

                self.items.append(ager)


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


QUALITY_RATES = {
    'basic_item': {
        'threshold_rates': {
                0: -1
        },
        'final_rate': -2
    },
    "Aged Brie": {
        'threshold_rates': {
                0: 1
        },
        'final_rate': 2
    },

}











class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

