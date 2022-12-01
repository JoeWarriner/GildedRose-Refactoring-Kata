from __future__ import annotations
from abc import ABC, abstractmethod
from item_updaters import Item, ItemUpdater, BasicItemUpdater, SPECIAL_UPDATERS
# -*- coding: utf-8 -*-



class GildedRose(object):
    items: list[ItemUpdater]

    def __init__(self, items: list[Item]):
        self.items = []
        for item in items:
            try:
                updater = SPECIAL_UPDATERS[item.name](item)
            except KeyError:
                updater = BasicItemUpdater(item)

            self.items.append(updater)


    def update_quality(self):
        for item in self.items:
            item.update_quality()






