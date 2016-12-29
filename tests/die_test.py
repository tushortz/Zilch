import unittest

from zilch.die import Die


class TestDieMethods(unittest.TestCase):
    def test_die(self):
        die_faces = list(range(1, 7))
        roll = Die().roll()
        die_is_valid = roll in die_faces
        self.assertTrue(die_is_valid)


if __name__ == '__main__':
    unittest.main()