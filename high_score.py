#-----------------------------
# Brody Miller
# 10/19/26
# high score game
#-----------------------------

#benefits of using a external file:
#it allows the players high score to be saved
# even once the program is closed. without an
# external file the high score would reset
# every single time the game is run

# the text file keeps the highest score achieved.
# the program reads the score when it is opened
# and will update the file everytime the high
#score is beat

# external files allow information to be able to
# be changed without changing the code everytime
# and keeps data saved seperately from the
# program


import random

file_name = "high-score.txt"


def load_high_score():
    try:
        with open(file_name, "r") as file:
            return int(file.read().strip() or 0)
    except (FileNotFoundError, ValueError):
        return 0


def save_high_score(score):
    with open(file_name, "w") as file:
        file.write(str(score))


def play_game():
    number = random.randint(1, 10)
    attempts = 0

    print("\nGuess a number between 1 and 10!")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 10:
                print("Please choose a number between 1 and 10.")
            elif guess < number:
                print("Too low!")
            elif guess > number:
                print("Too high!")
            else:
                score = max(1, 11 - attempts)
                print(f"\nCorrect! The number was {number}.")
                print(f"Attempts: {attempts}")
                print(f"Your score: {score}")
                return score

        except ValueError:
            print("Please enter a whole number.")


def main():
    print("=== HIGH SCORE GUESSING GAME ===")

    high_score = load_high_score()
    print(f"Current high score: {high_score}")

    score = play_game()

    if score > high_score:
        print("Congratulations! You got a new high score!")
        save_high_score(score)
        print("Your high score has been saved!")
    else:
        print("You didn't beat the high score. Womp womp!")

    print("Thanks for playing!")


if __name__ == "__main__":
    main()