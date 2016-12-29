from random import randint


class UnexpectedDieError(Exception):
    """
        Die exception class
    """

    def __init__(self, player, die):
        self.player = player
        self.die = die


class Die:
    """
        Die class representing the six die faces of a normal dice
    """

    def __init__(self, value=None, number_of_sides=6):
        self.number_of_sides = number_of_sides

        if type(value) == int:
            self.value = value
        else:
            self.value = self.roll()

    def __repr__(self):
        return str(self.value)

    def __str__(self):
        return str(self.value)

    def __eq__(self, die_to_compare):

        if self.get_value() == die_to_compare:
            return 0
        elif self.get_value() > die_to_compare:
            return 1
        else:
            return -1

    def __lt__(self, die_to_compare):
        if self.get_value() == die_to_compare:
            return 0
        elif self.get_value() > die_to_compare:
            return 1
        else:
            return -1

    def __gt__(self, die_to_compare):
        if self.get_value() == die_to_compare:
            return 0
        elif self.get_value() > die_to_compare:
            return 1
        else:
            return -1

    def roll(self):
        self.value = randint(1, self.number_of_sides)
        return self.value

    def get_value(self):
        return self.value

    def get_number_of_sides(self):
        return self.number_of_sides
