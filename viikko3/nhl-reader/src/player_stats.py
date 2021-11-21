class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        players = self.reader.get_players()
        players.sort(reverse=True, key=lambda player: player.assists+player.goals)
        nat_players = filter(lambda player : player.nationality == nationality, players)
        return nat_players