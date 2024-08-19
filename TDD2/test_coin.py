import unittest
from unittest import TestCase

import coin

class TestCoin(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.coin =coin.Coin()

    def test_coin_one(self):
        num = 1
        self.assertEqual(True, self.coin.coin_game(num))

    def test_coin_two(self):
        num = 2
        self.assertEqual(True, self.coin.coin_game(num))

    def test_coin_tree(self):
        num = 3
        self.assertEqual(False, self.coin.coin_game(num))

    def test_coin_four(self):
        num = 4
        self.assertEqual(True, self.coin.coin_game(num))

    def test_coin_six(self):
        num = 6
        self.assertEqual(False, self.coin.coin_game(num))
