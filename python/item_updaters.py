from __future__ import annotations
from abc import ABC, abstractmethod


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class ItemUpdater(ABC):
    def __init__(self, item: Item):
        self.item = item

    @abstractmethod
    def update_quality(self) -> None:
        ...

class BasicItemUpdater(ItemUpdater):


    def update_quality(self):
        ''' Update quality of item'''
        self.item.sell_in -= 1
        if self.item.sell_in >= 0:
            self.item.quality -= 1
        else:
            self.item.quality -= 2
        if self.item.quality < 0:
            self.item.quality = 0


class AgedBrieUpdater(ItemUpdater):


    def update_quality(self):
        self.item.sell_in -= 1
        if self.item.sell_in >= 0:
            self.item.quality += 1
        else:
            self.item.quality +=2

        if self.item.quality > 50:
            self.item.quality = 50


class SulfurasUpdater(ItemUpdater):

    def update_quality(self):
        pass

class BackstageUpdater(ItemUpdater):

    def update_quality(self) -> None:
        self.item.sell_in -= 1

        if self.item.sell_in >= 10:
            self.item.quality += 1
        elif self.item.sell_in >= 5:
            self.item.quality += 2
        elif self.item.sell_in >= 0:
            self.item.quality += 3
        else:
            self.item.quality = 0

        if self.item.quality > 50:
            self.item.quality = 50


SPECIAL_UPDATERS = {
    'Aged Brie': AgedBrieUpdater,
    'Sulfuras, Hand of Ragnaros': SulfurasUpdater,
    'Backstage passes to a TAFKAL80ETC concert': BackstageUpdater
}
