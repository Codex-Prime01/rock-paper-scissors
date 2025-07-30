import random

print("Welcome to Rock, Paper, Scissors!")

while True:
    options = ["r", "p", "s"]
    computer_choice = random.choice(options)
    user_choice = input("Rock, Paper or Scissors? (r/p/s): ").lower()

    if user_choice not in options:
        print("Invalid choice. Please select r, p, or s.")
        continue

    choices = {"r": "⚫ Rock", "p": "📑 Paper", "s": "✂ Scissors"}
    print(f"You chose: {choices[user_choice]}")
    print(f"Computer chose: {choices[computer_choice]}")

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a draw 🤗")
    elif (
        (user_choice == "r" and computer_choice == "s") or
        (user_choice == "p" and computer_choice == "r") or
        (user_choice == "s" and computer_choice == "p")
    ):
        print("You win! 🎉")
    else:
        print("Computer wins! 😮")

    cont = input("Do you want to play again? (y/n): ").lower()
    if cont != "y":
        print("Thanks for playing!")
        break
