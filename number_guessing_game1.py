import random
import json

def get_players():
    num_players = int(input("Enter no of players: "))
    players = []

    for i in range(num_players):
        name = input("Enter player name: ")
        players.append({"name": name, "score": 0})

    return players


def play_game(player):
    actual = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    while attempts < max_attempts:
        try:
            guess = int(input(f"{player['name']}, guess (1-100): "))
        except ValueError:
            print("Invalid input")
            continue

        if guess < 1 or guess > 100:
            print("Out of range")
            continue

        attempts += 1

        if guess == actual:
            print(f"{player['name']} wins in {attempts} attempts!")
            return attempts
        elif guess < actual:
            print("Too low")
        else:
            print("Too high")

    print(f"{player['name']} lost. Number was {actual}")
    return attempts


def update_leaderboard(players):
    players.sort(key=lambda x: x['score'])
    print("\nLeaderboard:")
    for p in players:
        print(f"{p['name']}: {p['score']} attempts")


def save_leaderboard(players):
    with open("leaderboard.json", "w") as f:
        json.dump(players, f)


def load_leaderboard():
    try:
        with open("leaderboard.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def main():
    players = get_players()

    for player in players:
        player['score'] = play_game(player)

    existing = load_leaderboard()
    existing.extend(players)

    existing.sort(key=lambda x: x['score'])
    existing = existing[:5]

    update_leaderboard(existing)
    save_leaderboard(existing)


if __name__ == "__main__":
    main()
