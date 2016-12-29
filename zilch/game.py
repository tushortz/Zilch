from zilch.die import UnexpectedDieError
from zilch.scoreboard import ScoreBoard


class Game:
    """
        Game engine class for Zilch
    """

    def __init__(self):
        self.board = None

    def play_turn_for_each_player(self, from_index, to_index, players, board, stop_when_threshold_met):
        """
        :rtype: Returns the last player position in the list
        """
        end_game = False
        last_player_index = -1

        while not end_game and from_index <= to_index:
            try:

                # Play a turn for the player and add their score to the score board.
                turn_score = players[from_index].play_turn(board)
                board.add_to_score(players[from_index], turn_score)

                if stop_when_threshold_met:
                    # Check whether the player has scored the threshold score for finishing the game.
                    end_game = board.get_score(players[from_index]) >= ScoreBoard.FINISH_THRESHOLD

                    if end_game:
                        last_player_index = from_index

            except UnexpectedDieError as err:
                print(err)

            from_index += 1

        return last_player_index

    def get_score_board(self):
        return self.board

    def play(self, players):
        self.board = ScoreBoard(players)

        # Play multiple turns until one player meets the end game threshold.
        last_player_index = -1

        while last_player_index < 0:
            # Play a turn for each player.
            last_player_index = self.play_turn_for_each_player(0, len(players) - 1, players, self.board, True)

            # Play the last turn.  Start with the next player index and allow everyone one last turn.
            if last_player_index == len(players) - 1:
                # The last player in the list is the one which passed the threshold
                # so run through all players from start to end.
                self.play_turn_for_each_player(0, len(players) - 1, players, self.board, False)
            else:
                # Run through the next player to the end of the list.
                self.play_turn_for_each_player(last_player_index + 1, len(players) - 1, players, self.board, False)

                # Run through the start of the list to the person who surpassed the threshold.
                self.play_turn_for_each_player(0, last_player_index, players, self.board, False)

        return self.board.get_winning_player()
