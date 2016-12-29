from zilch.die import Die, UnexpectedDieError
from zilch.scorer import Scorer


class Player:
    """
        Player class representing each zilch player object
    """

    def __init__(self, name, tactics, chatty=False):
        self.name = name
        self.tactics = tactics
        self.chatty = chatty

    def __repr__(self):
        return self.name

    def get_name(self):
        return self.name

    def reset(self, dice_to_reset):
        # Clear out the contents and add 6 new dice.
        dice_to_reset.clear()

        for i in range(6):
            dice_to_reset.append(Die())

        return dice_to_reset

    def play_turn(self, scoreboard):
        if self.chatty:
            print("Starting turn for %s player" % self.name)

        score = 0
        turn_ended = False
        dice = []

        # Play multiple rounds until either no scoring dice are thrown or the decision
        # is made to stop the turn
        while not turn_ended:
            # If there are no dice to roll then reset to 6. This can happen
            # if all 6 dice have been kept for scoring or at the start of the turn
            if len(dice) == 0:
                dice = self.reset(dice)

            # Shake the dice
            self.roll(dice)

            if self.chatty:
                print("%s player rolled %s" % (self.name, dice))

            # The turn is finished immediately if no scoring dice have been thrown
            if Scorer().score(dice).number_of_dice_used == 0:
                # The most recent throw produced no scoring dice
                # The turn is over and any score achieved so far is wiped out
                score = 0
                turn_ended = True

                if self.chatty:
                    print("No scoring dice for %s player. Turn ended" % self.name)

            else:
                # Ask the tactics which dice should be scored
                dice_to_score = self.tactics.select_dice_to_keep(list(dice))

                if self.chatty:
                    print("Player kept %s for scoring" % list(dice_to_score))

                # If no dice have been returned for scoring then the turn should be terminated
                if dice_to_score is None or len(dice_to_score) == 0:
                    if self.chatty:
                        print("No dice returned for scoring by %s player so turn is finished" % self.name)
                    turn_ended = True

                if not turn_ended:
                    # Remove the dice which are to be scored from those which are available to shake
                    for die in dice_to_score:
                        if die is not None:
                            try:
                                dice.remove(die)
                                dice_is_removed = True
                            except ValueError:
                                dice_is_removed = False

                            if not dice_is_removed:
                                # A die has been returned to be scored which was not in the dice
                                # sent to the tactics class to be considered for keeping
                                # This is either an attempt to cheat or a bug in the tactics code.
                                # Either way, an exception will be thrown and the turn terminated
                                if self.chatty:
                                    print("Unexpected die returned for scoring by %s player with a value of %s" % (
                                        self.name, die))
                                raise UnexpectedDieError(self, die)

                    # Score the dice
                    round_score = Scorer().score(dice_to_score)
                    if self.chatty:
                        print("Round score %s for %s player" % (round_score.score, self.name))

                    score += round_score.score

                    if self.chatty:
                        print("Turn score so far %s for %s player" % (score, self.name))

                    # If the tactics chose to keep dice which didn't score anything then the turn is finished
                    if round_score.number_of_dice_used < len(dice_to_score):
                        if self.chatty:
                            print("Player %s chose to keep dice which didn't score and so the turn is finished"
                                  % self.name)

                        turn_ended = False

                    else:
                        dice_size = len(dice)
                        if dice_size == 0:
                            dice_size = 6

                        # Check whether the turn should be finished
                        turn_ended = self.tactics.has_finished_turn(score, dice_size, self, scoreboard)

                        if turn_ended and self.chatty:
                            print("%s player has ended their turn" % self.name)

        if self.chatty:
            print("Turn score for %s player was %s" % (self.name, score))

        return score

    def roll(self, dice_to_roll):
        for die in dice_to_roll:
            die.roll()
