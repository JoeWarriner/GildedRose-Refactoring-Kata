# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):

    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

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

        

if __name__ == '__main__':
    unittest.main()
