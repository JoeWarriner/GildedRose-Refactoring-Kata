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
            if item.name != "Sulfuras, Hand of Ragnaros":
                self._update_quality(item)
                self._update_sell_in(item)


    def _update_quality(self, item):
        item_has_special_conditions = item.name == "Aged Brie" or item.name == "Backstage passes to a TAFKAL80ETC concert"

        
        if not item_has_special_conditions:
            if item.quality > 0:
                    item.quality = item.quality - 1
            if item.sell_in < 1 :
                if item.quality > 0:
                    item.quality = item.quality - 1


        if item_has_special_conditions:
            if item.quality < 50:
                item.quality = item.quality + 1
                if item.name == "Backstage passes to a TAFKAL80ETC concert":
                    if item.sell_in < 11:
                        if item.quality < 50:
                            item.quality = item.quality + 1
                    if item.sell_in < 6:
                        if item.quality < 50:
                            item.quality = item.quality + 1
            if item.sell_in < 1:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        pass
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1

    def _update_sell_in(self, item):
        item.sell_in = item.sell_in - 1




class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
