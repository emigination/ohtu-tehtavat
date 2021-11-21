import requests
from player import Player

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    response = requests.get(url).json()

    print("JSON-muotoinen vastaus:")
    print(response)

    players = []

    for player_dict in response:
        player = Player(player_dict)

        players.append(player)

    print("Oliot:")

    for player in players:
        if player.nationality == "FIN": print(player)

if __name__ == "__main__":
    main()
