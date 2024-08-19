import unittest
import candy2

class TestCandy(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.candy = candy2.Candy2()

    def test_empty_line_give_zero(self):
        child = []
        self.assertEqual(0, self.candy.give_candies(child))

    def test_one_child_give_one_candy(self):
        child = [99]
        self.assertEqual(1, self.candy.give_candies(child))

    # def test_two_children_have_same_ratings_give_two_candies(self):
    #     child = [1, 1]
    #     self.assertEqual(2, self.candy.give_candies(child))
    #
    # def test_two_child_have_not_same_ratings_give_three_candies(self):
    #     child = [1, 2]
    #     self.assertEqual(3, self.candy.give_candies(child))
    #
    # def test_three_child_have_not_same_rating_give_four_candies(self):
    #     child = [1,2,2]
    #     self.assertEqual(4, self.candy.give_candies(child))
    #
    # def test_three_child_have_not_same_rating_give_five_candies(self):
    #     child = [1,2,3]
    #     self.assertEqual(5, self.candy.give_candies(child))

