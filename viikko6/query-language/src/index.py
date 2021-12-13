from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, All, Not, HasFewerThan, Or

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    matcher = Or(
        HasAtLeast(30, "goals"),
        HasAtLeast(50, "assists")
    )

    for player in stats.matches(matcher):
        print(player)

    matcher = And(
        HasFewerThan(1, "goals"),
        PlaysIn("NYR")
    )


if __name__ == "__main__":
    main()