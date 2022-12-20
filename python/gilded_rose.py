# -*- coding: utf-8 -*-

"""
Strategy:
- Break update_quality mega method into smaller methods, within GildedRose class.
- Then we are likely to end up with a very big class, so further break that into smaller classes.
- Ulimately aim for OOP solution, but don't require strict OOP principles for initial changes.
"""

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                pass
            elif item.name == "Aged Brie":
                self._update_quality_aged_brie(item)
                self._update_sell_in(item)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                self._update_quality_backstage_pass(item)
                self._update_sell_in(item)
            else:
                self._update_quality_basic(item)
                self._update_sell_in(item)


    def _update_quality_basic(self, item):
        if item.quality > 0:
            item.quality = item.quality - 1
        if item.sell_in < 1 :
            if item.quality > 0:
                item.quality = item.quality - 1

    def _update_quality_aged_brie(self, item):
        if item.quality < 50:
                item.quality = item.quality + 1
        if item.sell_in < 1:
            if item.quality < 50:
                item.quality = item.quality + 1

    def _update_quality_backstage_pass(self, item):
        if item.quality < 50:
            item.quality = item.quality + 1
        if item.sell_in < 11:
            if item.quality < 50:
                item.quality = item.quality + 1
        if item.sell_in < 6:
            if item.quality < 50:
                item.quality = item.quality + 1
        if item.sell_in < 1:
            item.quality = item.quality - item.quality



    def _update_sell_in(self, item):
        item.sell_in = item.sell_in - 1




class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
