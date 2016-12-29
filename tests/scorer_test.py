import unittest

from zilch.die import Die
from zilch.scorer import Scorer


class TestScorerMethod(unittest.TestCase):
    def test_score_one_of_a_kind(self):
        die_value = Die(6).get_value()
        value = Scorer().score_one_of_a_kind(die_value).score
        self.assertEqual(value, 0)

        die_value = Die(1).get_value()
        value = Scorer().score_one_of_a_kind(die_value).score
        self.assertEqual(value, 100)

        die_value = Die(5).get_value()
        value = Scorer().score_one_of_a_kind(die_value).score
        self.assertEqual(value, 50)

    def test_score_three_of_a_kind(self):
        die_value = Die(1).get_value()
        value = Scorer().score_three_of_a_kind(die_value).score
        self.assertEqual(value, 1000)

        die_value = Die(5).get_value()
        value = Scorer().score_three_of_a_kind(die_value).score
        self.assertEqual(value, 500)

    def test_score_four_of_a_kind_and_a_pair(self):
        die_value = [4, 2]
        value = Scorer().score_four_of_a_kind_and_a_pair(die_value).score
        print(value)
        self.assertEqual(value, 500)


if __name__ == '__main__':
    unittest.main()
