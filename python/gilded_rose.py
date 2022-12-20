# -*- coding: utf-8 -*-

"""
Strategy:
- Break update_quality mega method into smaller methods, within GildedRose class.
- Then we are likely to end up with a very big class, so further break that into smaller classes.
- Ulimately aim for OOP solution, but don't require strict OOP principles for initial changes.

"""

class GildedRose(object):

    def __init__(self, items):
        self.items = [UpdatableItem.create(item) for item in items]

    def update_quality(self):
        for item in self.items:
            item.update()



class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class UpdatableItem(Item):
    def __init__(self, item):
        self._item = item

    def update(self):
        self._update_quality()
        self._update_sell_in()

    def _update_sell_in(self):
        self._item.sell_in = self._item.sell_in - 1

    def _update_quality(self):
        pass

    def _increment_item_quality(self):
        if self._item.quality < 50:
            self._item.quality += 1

    def _decrement_item_quality(self):
        if self._item.quality > 0:
            self._item.quality -= 1

    @classmethod
    def create(cls, item):
        if item.name == "Sulfuras, Hand of Ragnaros":
            return Ragnaros(item)
        elif item.name == "Aged Brie":
            return AgedBrie(item)
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            return BackstagePass(item)
        else:
            return Basic(item)

class Basic(UpdatableItem):
    def _update_quality(self):
        self._decrement_item_quality()
        if self._item.sell_in < 1 :
            self._decrement_item_quality()


class AgedBrie(UpdatableItem):
    def _update_quality(self):
        self._increment_item_quality()
        if self._item.sell_in < 1:
            self._increment_item_quality()

class BackstagePass(UpdatableItem):

    def _update_quality(self):
        self._increment_item_quality()
        if self._item.sell_in < 11:
                self._increment_item_quality()
        if self._item.sell_in < 6:
                self._increment_item_quality()
        if self._item.sell_in < 1:
            self._item.quality = self._item.quality - self._item.quality

class Ragnaros(UpdatableItem):
    def _update_quality(self):
        pass

    def _update_sell_in(self):
        pass