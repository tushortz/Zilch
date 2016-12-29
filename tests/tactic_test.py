import unittest

from tactic.tactic import Tactic
from zilch.die import Die
from zilch.player import Player
from zilch.scoreboard import ScoreBoard


class TestTacticMethod(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.tactic = Tactic()
        self.dice = [Die() for i in range(6)]
        self.player = Player("Player", self.tactic, False)
        self.scoreboard = ScoreBoard([self.player])

    def test_die_to_keep_is_in_die_thrown(self):
        dice_to_keep = self.tactic.select_dice_to_keep(self.dice)
        actual = (all(x in self.dice for x in dice_to_keep))
        self.assertTrue(actual)

    def test_player_has_finished_turn(self):
        has_finished_turn_true = self.tactic.has_finished_turn(0, 2, self.player, self.scoreboard)
        has_finished_turn_false = self.tactic.has_finished_turn(10000, len(self.dice), self.player, self.scoreboard)

        self.assertTrue(has_finished_turn_true)
        self.assertFalse(has_finished_turn_false)


if __name__ == '__main__':
    unittest.main()
