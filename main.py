
import random

PROJECTS = [
    ("Password Generator", "Create a secure random password."),
    ("Number Guessing Game", "Guess a secret number."),
    ("Daily Quote", "Display a random motivational quote."),
    ("Rock Paper Scissors", "Play against the computer."),
    ("Mini Quiz", "Answer random trivia questions."),
    ("Word Scrambler", "Unscramble a randomly selected word."),
    ("Dice Roller", "Roll virtual dice for your next game."),
    ("To-Do List", "Manage a small list of daily tasks."),
    ("Coin Flipper", "Flip a virtual coin."),
    ("Story Generator", "Generate a silly random story idea."),
]


def main():
    print("\n=== Tiny Idea Generator ===")
    print("Need something to build? Here's an idea!\n")

    while True:
        name, description = random.choice(PROJECTS)
        print(f"💡 {name}")
        print(f"   {description}\n")

        again = input("Generate another idea? (y/n): ").strip().lower()
        if again != "y":
            print("Happy coding! 🚀")
            break


if __name__ == "__main__":
    main()
