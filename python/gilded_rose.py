from __future__ import annotations
# -*- coding: utf-8 -*-

SPECIAL_ITEMS = [
    "Backstage passes to a TAFKAL80ETC concert",
    "Sulfuras, Hand of Ragnaros"
]




class GildedRose(object):

    def __init__(self, items: list[Item]):
        self.items = []
        for item in items:
            if item.name not in SPECIAL_ITEMS:
                self.items.append(BasicItemAger(item))
            else:
                self.items.append(item)

    def update_quality(self):
        for item in self.items:
            if isinstance(item, BasicItemAger):
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


class BasicItemAger:

    def __init__(self, item: Item):
        self.item = item
        self.quality_rates = QUALITY_RATES[item.name] if item.name in QUALITY_RATES.keys() else QUALITY_RATES['basic_item']

    def update_quality_rate(self):
        '''Update rate of quality increase/decline based on item sell_in value'''

        if self.item.sell_in < min(self.quality_rates['threshold_rates'].keys()):
                self.quality_rate = self.quality_rates['final_rate']
        else:
            threshold = max( [t for t in self.quality_rates['threshold_rates'] if t <= self.item.sell_in])
            self.quality_rate = self.quality_rates['threshold_rates'][threshold]

    def update_quality(self):
        ''' Update quality of item'''
        self.item.sell_in -= 1
        self.update_quality_rate()
        try:
            new_quality = self.item.quality + self.quality_rate
            assert new_quality >= 0
        except AssertionError:
            new_quality = 0
        self.item.quality = new_quality








class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

