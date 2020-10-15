import random


def random_num():
    """
    Generates a random number between 1 and 10 with the use of the random module
    """
    num = random.randint(1, 10)
    return num


def player_guess():
    """
    Takes in and returns a number inputted by the user
    """
    while True:
        try:
            num = int(input("Enter a number between 1 and 10: "))

            # While the number is less than 1 or more than 11, prompts the user to enter a valid number
            while num not in range(1, 11):
                print("Number not in range!")
                num = int(input("Enter a number between 1 and 10: "))
            return num
        # If the value is anything but an integer, displays a warning message
        except ValueError:
            print("Invalid input!")


def is_guess_correct(player_num, computer_num):
    """
    Compares the user guessed number against the randomly generated number
    """
    if player_num == computer_num:
        return "Correct"
    elif player_num < computer_num:
        return "Go Higher"
    else:
        return "Go Lower!"


def play_game():
    """
    Runs the game of guess the number
    """
    # Boolean value to control the game
    in_progress = True

    # Prints an intro statement
    print("I'm thinking of a number between 1 and 10. What number am I thinking of?")

    # Generates a random number
    random_number = random_num()

    while in_progress:
        # Asks user to guess the number
        player_number = player_guess()
        print(f"You guessed {player_number}.")

        # Checks whether user guess equals random number
        check_for_win = is_guess_correct(player_number, random_number)

        if check_for_win == "Correct":
            print("Correct, that is the number I was thinking of. YOU WIN!")
            in_progress = False
        else:
            print(check_for_win)


play_game()

# Asks user if they would like to play again
while True:
    play_again = input("Would you like to play again? y/n: ")

    # While play_again is not y or n, prompts the user to provide the correct input
    while play_again.lower() not in ["y", "n"]:
        print("Invalid input!")
        play_again = input("Would you like to play again? y/n: ")
    # If y, calls the play_game() function
    if play_again.lower() == "y":
        play_game()
    # If n, ends the program
    else:
        print("Thanks for playing!")
        break
