class ScoreBoard:
    MIN_THRESHOLD = 1000
    FINISH_THRESHOLD = 10000

    def __init__(self, players):
        # Set the score board up with starting scores of zero
        self.scores = dict()
        for player in players:
            self.scores[player] = 0

    def __str__(self):
        return "Scoreboard: %s" % self.scores

    def get_score(self, player):
        return int(self.scores.get(player))

    def get_all_players(self):
        return list(self.scores.keys())

    def get_all_scores(self):
        scores = self.scores.values()
        return_scores = []
        return_index = 0

        for score in scores:
            return_scores[return_index] = int(score)
            return_index += 1

        return return_scores

    def get_winning_player(self):
        # Find the player with the highest score
        """

        :rtype: Returns the winning player (Player object) of the round. (
        """
        winning_player = None
        winning_score = -1
        players = self.get_all_players()

        for player in players:
            if self.get_score(player) > winning_score:
                winning_score = self.get_score(player)
                winning_player = player

        return winning_player

    def add_to_score(self, player, score_to_add):
        existing_score = int(self.scores.get(player))
        total_score = existing_score + score_to_add

        # Check that the score meets the minimum threshold.  If not set it to zero
        if total_score < self.MIN_THRESHOLD:
            total_score = 0

        self.scores[player] = total_score

        return total_score
