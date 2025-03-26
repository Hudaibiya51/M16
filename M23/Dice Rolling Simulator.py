import random

def roll_dice():
    return random.randint(1, 6)

def dice_roller():
    print("Welcome to the Dice Rolling Simulator!")
    while True:
        input("Press Enter to roll the dice or type 'exit' to quit: ")
        
        # Roll the dice and display the result
        result = roll_dice()
        print(f"You rolled a {result}!")
        
        # Option to continue or exit
        choice = input("Do you want to roll again? (y/n): ").lower()
        if choice != 'y':
            print("Thanks for playing! Goodbye!")
            break

# Start the Dice Rolling Simulator
dice_roller()
