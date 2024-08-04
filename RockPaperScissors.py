import random

def get_computer_choice():
    """Randomly select a choice for the computer."""
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on the choices."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "You lose!"

def get_user_choice():
    """Get the user's choice."""
    while True:
        choice = input("Enter rock, paper, or scissors: ").lower()
        if choice in ['rock', 'paper', 'scissors']:
            return choice
        else:
            print("Invalid choice. Please enter rock, paper, or scissors.")

def display_instructions():
    """Display instructions for the game."""
    print("\nWelcome to Rock, Paper, Scissors!")
    print("Here are the rules:")
    print(" - Rock beats Scissors")
    print(" - Scissors beats Paper")
    print(" - Paper beats Rock")
    print("Type your choice when prompted.")

def play_game():
    """Play multiple rounds of Rock, Paper, Scissors."""
    user_score = 0
    computer_score = 0

    display_instructions()

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\nYour choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1

        print(f"Score - You: {user_score} | Computer: {computer_score}")

        # Ask if the player wants to play again
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again not in ['yes', 'y']:
            print("\nThanks for playing!")
            break

if __name__ == "__main__":
    play_game()
