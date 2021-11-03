import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_player_is_found(self):
        player = self.statistics.search('Kurri')
        self.assertEqual(player.name, 'Kurri')

    def test_nonexistent_player_not_found(self):
        player = self.statistics.search('kissa')
        self.assertIsNone(player)

    def test_team_returns_team_members(self):
        team = self.statistics.team('EDM')
        self.assertEqual({team[0].name, team[1].name, team[2].name}, {'Semenko', 'Kurri', 'Gretzky'})

    def test_correct_top_scorers(self):
        top = self.statistics.top_scorers(2)
        self.assertEqual({top[0].name, top[1].name}, {'Lemieux', 'Gretzky'})
