# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):

    # Basic Items - Requirements

    def test_basic_item_single_day(self):
        test_item = Item("test_item", 2, 2)
        gilded_rose = GildedRose([test_item])
        gilded_rose.update_quality()
        self.assertEqual(test_item.sell_in, 1)
        self.assertEqual(test_item.quality, 1)

    def test_basic_item_multiple_days(self):
        test_item = Item("test_item", 5, 5)
        gilded_rose = GildedRose([test_item])
        for i in range(4,-1,-1):
            gilded_rose.update_quality()
            self.assertEqual(test_item.sell_in, i)
            self.assertEqual(test_item.quality, i)

    def test_quality_after_sell_by_date(self):
        test_item = Item("test_item", 1, 5)
        gilded_rose = GildedRose([test_item])
        for i in [4, 2, 0]:
            gilded_rose.update_quality()
            self.assertEqual(test_item.quality, i)

    def test_quality_after_sell_by_date(self):
        test_item = Item("test_item", 1, 5)
        gilded_rose = GildedRose([test_item])
        for i in [4, 2, 0]:
            gilded_rose.update_quality()
            self.assertEqual(test_item.quality, i)

    def test_quality_never_negative(self):
        test_item = Item("test_item", 0, 0)
        gilded_rose = GildedRose([test_item])
        for i in [0, 0, 0]:
            gilded_rose.update_quality()
            self.assertEqual(test_item.quality, i)


    # Basic items - unspecified behaviour

    def test_sell_in_after_date(self):
        '''
        Q: What happens to sell in value after 0?
        A: Continues to decrease
        '''
        test_item = Item("test_item", 0, 0)
        gilded_rose = GildedRose([test_item])
        for i in [-1, -2, -3]:
            gilded_rose.update_quality()
            self.assertEqual(test_item.sell_in, i)

    def test_item_over_50(self):
        '''
        Q: What happens if you create and then update an item with more than 50 quality?
        (Specified max)
        A: It decreases anyway. (current behaviour)
        TODO: Add input validation.
        '''
        test_item = Item("test_item", 10, 70)
        gilded_rose = GildedRose([test_item])
        for i in [69, 68, 67]:
            gilded_rose.update_quality()
            self.assertEqual(test_item.quality, i)


    # Aged Brie - requirements

    def test_quality_aged_brie_qual_increase(self):
        test_item = Item("Aged Brie", 3, 0)
        gilded_rose = GildedRose([test_item])
        for i in [1, 2, 3]:
            gilded_rose.update_quality()
            self.assertEqual(test_item.quality, i)

    def test_quality_aged_brie_qual_increase(self):
        test_item = Item("Aged Brie", 3, 0)
        gilded_rose = GildedRose([test_item])
        for i in [1, 2, 3]:
            gilded_rose.update_quality()
            self.assertEqual(test_item.quality, i)

    # Aged Brie - unspecified behaviour

    def test_quality_aged_brie_qual_increase_after_date(self):
        '''Does Aged Brie increase double after date? Yes'''
        test_item = Item("Aged Brie", 0, 0)
        gilded_rose = GildedRose([test_item])
        for i in [2, 4, 6]:
            gilded_rose.update_quality()
            self.assertEqual(test_item.quality, i)


    # Sulfuras - requirements

    def test_sulfuras(self):
        test_item = Item("Sulfuras, Hand of Ragnaros", 20, 45)
        gilded_rose = GildedRose([test_item])
        for _ in range(1000):
            gilded_rose.update_quality()
            self.assertEqual(test_item.quality, 45)
            self.assertEqual(test_item.sell_in, 20)

    # Backstage passes - requirements:

    def test_backstage_passes(self):
        test_item = Item("Backstage passes to a TAFKAL80ETC concert", 15, 0)
        gilded_rose = GildedRose([test_item])
        for i in [1,2,3,4,5,7,9,11,13,15, 18, 21, 24, 27, 30, 0, 0, 0]:
            gilded_rose.update_quality()
            self.assertEqual(test_item.quality, i)


    # Conjured item:

    def test_conjured_item(self):
        test_item = Item("Conjured", 2, 20)
        gilded_rose = GildedRose([test_item])
        for i in [18, 16, 12, 8, 4, 0, 0, 0]:
            gilded_rose.update_quality()
            self.assertEqual(test_item.quality, i)


if __name__ == '__main__':
    unittest.main()
