class Tactic:
    """
        Tactic class that determines what tactics player should use
    """

    def select_dice_to_keep(self, dice):
        selected_die = self.get_second_selected_die(dice)

        if len(selected_die) > 0:
            die1 = self.get_die_with_value(dice, selected_die[0].get_value())

            if len(die1) > 0:
                second_selected_die = self.get_second_selected_die(die1)
                if len(second_selected_die) > 0:
                    if len(selected_die) == 6:
                        return selected_die

                    return self.join_dice(selected_die, second_selected_die)

                return self.join_dice(selected_die, self.get_die_with_value2(die1, 1))

            else:
                return selected_die

        if len(dice) == 6:
            if self.get_die_once(dice) or self.count_ones(dice):
                return dice

        ones = self.get_die_with_value2(dice, 1)
        if len(ones) == 0:
            return self.get_die_with_value2(dice, 5)

        return ones

    def has_finished_turn(self, turn_score, dice_available_to_throw, player, scoreboard):
        player_score = scoreboard.get_score((player))

        if player_score == 0:
            if turn_score >= 1000 and dice_available_to_throw > 3:
                return False
            else:
                return True

        elif player_score >= 10000:
            return True
        elif dice_available_to_throw == 5 or dice_available_to_throw == 4:
            return turn_score >= 800
        elif dice_available_to_throw == 3:
            return turn_score >= 300
        elif dice_available_to_throw == 2:
            return turn_score >= 200
        elif dice_available_to_throw == 1:
            return True
        else:
            return False

    def get_second_selected_die(self, rolled_dice):
        best_value = 0
        the_value = 0
        highscore = 0
        scoring_dice = []

        for i in range(1, 7):
            if i == 1:
                best_value = 1000
            else:
                best_value = i * 100

            dice = self.get_die_with_value2(rolled_dice, i)

            if len(dice) >= 3:
                the_value = best_value * self.get_increment(len(dice))

                if the_value > highscore:
                    highscore = the_value

                    for die in dice:
                        scoring_dice.append(die)

        return scoring_dice

    def get_die_with_value(self, rolled_dice, get_dice_value):
        """
        :rtype: list of die object
        """
        scoring_dice = []

        for die in rolled_dice:
            dice_value = die.get_value()

            if dice_value != get_dice_value:
                scoring_dice.append(die)

        return scoring_dice

    def get_die_with_value2(self, rolled_dice, get_dice_value):
        scoring_dice = []

        for die in rolled_dice:
            dice_value = die.get_value()

            if dice_value == get_dice_value:
                scoring_dice.append(die)

        return scoring_dice

    def get_second_selected_die_value(self, rolled_dice):
        best_value = 0
        the_value = 0
        highscore = 0

        for i in range(1, 7):
            if i == 1:
                best_value = 1000
            else:
                best_value = i * 100

            dice = self.get_die_with_value2(rolled_dice, i)

            if len(dice) >= 3:
                the_value = best_value * self.get_increment(len(dice))

        return max(highscore, the_value)

    def join_dice(self, dice_list1, dice_list2):
        return dice_list1 + dice_list2

    def get_die_once(self, rolled_dice):
        rolled_dice = sorted(rolled_dice)

        if (rolled_dice[0].get_value() == rolled_dice[1] and
                    rolled_dice[2].get_value() == rolled_dice[3] and
                    rolled_dice[4].get_value() == rolled_dice[5]):
            return True

        return False

    def get_increment(self, a):
        if a == 3:
            return 1
        elif a == 4:
            return 2
        elif a == 5:
            return 4
        else:
            return 8

    def count_ones(self, dice):
        dice = sorted(dice)
        return str(dice) == "[1, 2, 3, 4, 5, 6]"
