import unittest

from tactic.tactic import Tactic


class TestTacticMethod(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.tactic = Tactic()

    def test_die(self):
        print(self.tactic)

if __name__ == '__main__':
    unittest.main()