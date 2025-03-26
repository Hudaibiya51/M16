import random

attempts_list = []

# Function to show the high score
def show_score():
    if len(attempts_list) == 0:  # Correcting the condition to check if attempts_list is empty
        print("There is currently no high score, it's yours for the taking!")
    else:
        print("The current high score is {} attempts".format(min(attempts_list)))

# Start the game function
def start_game():
    print("Hey There! Welcome to the game of guesses!")
    player_name = input("Enter your name: ")
    anna_play = input(f"Hi, {player_name}, would you like to play the guessing game? (Enter Yes/No): ")

    # Show the score before the game starts
    show_score()

    attempts = 0  # Resetting attempts for a new round
    random_number = random.randint(1, 10)  # Pick a random number between 1 and 10

    while anna_play.lower() == "yes":
        try:
            guess = input("Pick a number between 1 and 10: ")
            guess = int(guess)  # Convert input to integer

            if guess < 1 or guess > 10:
                raise ValueError("Please guess a number within the given range (1-10).")

            attempts += 1  # Increment attempts for each guess

            if guess == random_number:
                print(f"Congrats! You guessed it right in {attempts} attempts!")
                attempts_list.append(attempts)  # Store the number of attempts for the current game
                show_score()  # Show the high score
                play_again = input("Would you like to play again? (Enter Yes/No): ")
                if play_again.lower() == "no":
                    print("That's cool, have a nice day!")
                    break
                else:
                    # Reset the game for another round
                    attempts = 0
                    random_number = random.randint(1, 10)  # New random number
                    show_score()
            elif guess < random_number:
                print("It's lower! Try again.")
            else:
                print("It's higher! Try again.")

        except ValueError as err:
            print(f"Oh no! That's not a valid number. {err}. Please try again...")

    print("Goodbye, thank you for playing!")

# Run the game when the script is executed
if __name__ == '__main__':
    start_game()
