class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = player1_name
        self.player2 = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1:
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1

    def get_score(self):
        if self.player1_score == self.player2_score:
            return self._tie_score()
        if self.player1_score >= 4 or self.player2_score >= 4:
            return self._over_four_score()
        return self._score_to_word(self.player1_score) + '-' + self._score_to_word(self.player2_score)

    def _tie_score(self):
            if self.player1_score == 0:
                return "Love-All"
            if self.player1_score == 1:
                return "Fifteen-All"
            if self.player1_score == 2:
                return "Thirty-All"
            if self.player1_score == 3:
                return "Forty-All"
            return "Deuce"

    def _over_four_score(self):
            difference = self.player1_score - self.player2_score
            if difference == 1:
                return f"Advantage {self.player1}"
            if difference == -1:
                return f"Advantage {self.player2}"
            if difference >= 2:
                return f"Win for {self.player1}"
            return f"Win for {self.player2}"

    def _score_to_word(self, score):
            if score == 0:
                return "Love"
            elif score == 1:
                return "Fifteen"
            elif score == 2:
                return "Thirty"
            elif score == 3:
                return "Forty"
