class Scorer:
    def score(self, dice):
        if type(dice) == set or type(dice) == dict:
            return self.score(list(dice))

        # Score the dice as number of a kind
        number_of_a_kind_score = self.Score()
        value_count = [0] * 6

        for die in dice:
            # Get the count of dice with the same value as this one and increment
            if die is not None:
                value_count[die.get_value() - 1] += 1

        # Go through each of the possible dice values and score for number of a kind
        for loop in range(len(value_count)):
            latest_score = self.score_number_of_a_kind(value_count[loop], loop + 1)
            number_of_a_kind_score.score += latest_score.score
            number_of_a_kind_score.number_of_dice_used += latest_score.number_of_dice_used

        # Consider the special cases to see if they score more than the number of a kind score
        special_case_score1 = self.score_four_of_a_kind_and_a_pair(value_count)
        special_case_score2 = self.score_three_doubles(value_count)
        special_case_score3 = self.score_two_triples(value_count)
        special_case_score4 = self.score123456(value_count)

        score = self.maximum_dice_used([
            number_of_a_kind_score,
            special_case_score1,
            special_case_score2,
            special_case_score3,
            special_case_score4
        ])

        return score

    def score_number_of_a_kind(self, count, value):
        score = self.Score()

        if count == 1:
            score = self.score_one_of_a_kind(value)
        elif count == 2:
            score = self.score_two_of_a_kind(value)
        elif count == 3:
            score = self.score_three_of_a_kind(value)
        elif count == 4:
            score = self.score_four_of_a_kind(value)
        elif count == 5:
            score = self.score_five_of_a_kind(value)
        elif count == 6:
            score = self.score_six_of_a_kind(value)

        return score

    def score_one_of_a_kind(self, value):
        # 1 = 100 points
        # 5 = 50 points
        score = self.Score()

        if value == 1:
            score.score = 100
        elif value == 5:
            score.score = 50

        score.number_of_dice_used = 1
        return score

    def score_two_of_a_kind(self, value):
        # No special scoring for doubles so score each die separately
        score = self.Score()

        score.score = self.score_one_of_a_kind(value).score * 2
        if score.score > 0:
            score.number_of_dice_used = 2
        else:
            score.number_of_dice_used = 0

        return score

    def score_three_of_a_kind(self, value):
        score = self.Score()

        # Any triple = number x 100 points
        # The exception is when you have three 1’s = 1000 points
        if value == 1:
            score.score = 1000
        else:
            score.score = value * 100

        if score.score > 0:
            score.number_of_dice_used = 3
        else:
            score.number_of_dice_used = 0

        return score

    def score_four_of_a_kind(self, value):
        score = self.Score()

        # Any four of a kind = points scored for a triple x 2
        score.score = self.score_three_of_a_kind(value).score * 2

        if score.score > 0:
            score.number_of_dice_used = 4
        else:
            score.number_of_dice_used = 0

        return score

    def score_five_of_a_kind(self, value):
        score = self.Score()

        # Any five of a kind = points scored for four of a kind x 2
        score.score = self.score_four_of_a_kind(value).score * 2

        if score.score > 0:
            score.number_of_dice_used = 5
        else:
            score.number_of_dice_used = 0

        return score

    def score_six_of_a_kind(self, value):
        score = self.Score()

        # Any six of a kind = points scored for five of a kind x 2
        score.score = self.score_five_of_a_kind(value).score * 2

        if score.score > 0:
            score.number_of_dice_used = 6
        else:
            score.number_of_dice_used = 0

        return score

    def score_four_of_a_kind_and_a_pair(self, value_count):
        # A four of a kind and a pair (333322, for example) = 500 points
        score = self.Score()
        four_of_a_kind = False
        two_of_a_kind = False

        for value in value_count:
            if value == 4:
                four_of_a_kind = True
            elif value == 2:
                two_of_a_kind = True

        if four_of_a_kind and two_of_a_kind:
            score.score = 500
            score.number_of_dice_used = 6

        return score

    def score_three_doubles(self, value_count):
        # 3 doubles (221155, for example) = 500 points
        score = self.Score()
        double_count = 0

        for value in value_count:
            if value == 2:
                double_count += 1

            if double_count == 3:
                score.score = 500
                score.number_of_dice_used = 6

        return score

    def score_two_triples(self, value_count):
        # 2 triples (333222, for example) = 1000 points
        score = self.Score()
        triple_count = 0

        for value in value_count:
            if value == 3:
                triple_count += 1

        if triple_count == 2:
            score.score = 1000
            score.number_of_dice_used = 6

        return score

    def score123456(self, value_count):
        # 123456 = 2000 points
        score = self.Score()
        one_of_each = True

        for value in value_count:
            if value != 1:
                one_of_each = False

        if one_of_each:
            score.score = 2000
            score.number_of_dice_used = 6

        return score

    def maximum_dice_used(self, scores):
        # Sort the scores.  This will make them from the smallest to the largest.
        # A score is larger if the number of dice used is highest or the number of dice used
        # is joint highest and the score value is the highest of thise scores with the
        # highest number of dice used.
        scores = sorted(scores)
        return scores[len(scores) - 1]

    class Score:
        def __init__(self):
            self.score = 0
            self.number_of_dice_used = 0

        def __str__(self):
            return "%s:%s" % (self.score, self.number_of_dice_used)

        def __repr__(self):
            return "%s:%s" % (self.score, self.number_of_dice_used)

        def __gt__(self, score_to_compare):
            if self.number_of_dice_used > score_to_compare.number_of_dice_used:
                return_value = 1

            elif self.number_of_dice_used == score_to_compare.number_of_dice_used:
                if self.score > score_to_compare.score:
                    return_value = 1
                elif self.score == score_to_compare.score:
                    return_value = 0
                else:
                    return_value = -1
            else:
                return_value = -1

            return return_value

        def __lt__(self, score_to_compare):
            if self.number_of_dice_used > score_to_compare.number_of_dice_used:
                return_value = 1

            elif self.number_of_dice_used == score_to_compare.number_of_dice_used:
                if self.score > score_to_compare.score:
                    return_value = 1
                elif self.score == score_to_compare.score:
                    return_value = 0
                else:
                    return_value = -1
            else:
                return_value = -1

            return return_value

        def __eq__(self, score_to_compare):
            if self.number_of_dice_used > score_to_compare.number_of_dice_used:
                return_value = 1

            elif self.number_of_dice_used == score_to_compare.number_of_dice_used:
                if self.score > score_to_compare.score:
                    return_value = 1
                elif self.score == score_to_compare.score:
                    return_value = 0
                else:
                    return_value = -1
            else:
                return_value = -1

            return return_value

        def compare_to(self, score_to_compare):
            if self.number_of_dice_used > score_to_compare.number_of_dice_used:
                return_value = 1

            elif self.number_of_dice_used == score_to_compare.number_of_dice_used:
                if self.score > score_to_compare.score:
                    return_value = 1
                elif self.score == score_to_compare.score:
                    return_value = 0
                else:
                    return_value = -1
            else:
                return_value = -1

            return return_value
