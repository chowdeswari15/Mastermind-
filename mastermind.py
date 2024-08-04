import random

def get_digits(num):
    return [int(digit) for digit in str(num)]

def get_feedback(guess, actual):
    guess_digits = get_digits(guess)
    actual_digits = get_digits(actual)
    correct_digits = sum([1 for i in range(len(guess_digits)) if guess_digits[i] == actual_digits[i]])
    return correct_digits

def player_guess(number_length):
    while True:
        try:
            guess = int(input(f"Enter your {number_length}-digit guess: "))
            if len(str(guess)) == number_length:
                return guess
            else:
                print(f"Please enter a {number_length}-digit number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def play_round(player, number_length):
    if player == 1:
        actual_number = int(input("Player 1, enter a multi-digit number for Player 2 to guess: "))
    else:
        actual_number = random.randint(10**(number_length-1), 10**number_length - 1)
        print(f"Player 2 has chosen a {number_length}-digit number.")

    attempts = 0
    while True:
        attempts += 1
        guess = player_guess(number_length)
        if guess == actual_number:
            print(f"Correct! The number was {actual_number}. It took you {attempts} attempts.")
            return attempts
        else:
            correct_digits = get_feedback(guess, actual_number)
            print(f"{correct_digits} digits are correct.")

def main():
    number_length = int(input("Enter the number of digits for the game: "))
    print("Player 1 will go first.")
    attempts_player1 = play_round(1, number_length)
    print("Now it's Player 2's turn.")
    attempts_player2 = play_round(2, number_length)

    if attempts_player1 < attempts_player2:
        print(f"Player 1 guessed the number in {attempts_player1} attempts.")
        print(f"Player 2 guessed the number in {attempts_player2} attempts.")
        print("Player 1 wins the game and is crowned Mastermind!")
    elif attempts_player1 > attempts_player2:
        print(f"Player 1 guessed the number in {attempts_player1} attempts.")
        print(f"Player 2 guessed the number in {attempts_player2} attempts.")
        print("Player 2 wins the game and is crowned Mastermind!")
    else:
        print(f"Both players guessed the numbers in {attempts_player1} attempts.")
        print("It's a tie!")

if __name__ == "__main__":
    main()
