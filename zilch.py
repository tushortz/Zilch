# Created by Taiwo Kareem
# 29-12-2016
# A Python implementation of a java version

from tactic.tactic import Tactic
from zilch.game import Game
from zilch.player import Player


def add_player(name, tactics, win_count, players, chatty):
    player = Player(name, tactics, chatty)
    players.append(player)
    win_count[player] = 0


def main(number_of_games, chatty):
    win_count = dict()
    players = []
    tactic = Tactic()

    # Add all players
    add_player("John Doe", tactic, win_count, players, chatty)
    add_player("Michael Jones", tactic, win_count, players, chatty)

    for rounds in range(number_of_games):
        # Play game
        game = Game()
        round_winner = game.play(players)

        # Record the winner
        player_win_count = win_count.get(round_winner)
        win_count[round_winner] = player_win_count + 1

        if chatty:
            print("The winner is %s." % game.get_score_board())

    winner = max_key = max(win_count, key=lambda k: win_count[k])

    print("Final results after %s game(s): %s" % (number_of_games, win_count))
    print("The winner of the current game is '%s'" % winner)


if __name__ == "__main__":
    main(10, False)
