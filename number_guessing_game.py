import random

def get_number_and_attempts(level):
    if level == "easy":
        return random.randint(1, 50), 10
    elif level == "medium":
        return random.randint(1, 100), 7
    else:
        return random.randint(1, 200), 5

def play_game():
    level = input("Choose level (easy/medium/hard): ").lower()
    actual, max_attempts = get_number_and_attempts(level)

    attempts = 0

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
        except:
            print("Invalid input")
            continue

        attempts += 1

        if guess == actual:
            print("Correct!")
            score = (max_attempts - attempts + 1) * 10
            print("Score:", score)
            return score
        elif guess < actual:
            print("Low")
        else:
            print("High")

    print("You lost. Number was:", actual)
    return 0


def update_leaderboard(leaderboard, score):
    leaderboard.append(score)
    leaderboard.sort(reverse=True)
    return leaderboard[:5]


def main():
    leaderboard = []

    while True:
        score = play_game()
        leaderboard = update_leaderboard(leaderboard, score)

        print("\nTop Scores:", leaderboard)

        again = input("Play again? (yes/no): ").lower()
        if again != "yes":
            break

main() 
