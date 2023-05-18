import random

def main():
    choices = ['rock', 'paper', 'scissors']

    # user input to challenge computer
    answer = input("You dare challenge me to a game of rock, paper, scissors [y/n]: ").lower()

    while answer == 'y':
        print("\nVery well, let's begin!")
        user_choice = input("Type your choice: rock, paper, or scissors: ").lower()

        # check for valid input
        while user_choice not in choices:
            user_choice = input("Invalid choice. Please enter rock, paper, or scissors: ").lower()

        computer_choice = random.choice(choices)

        # determines winner
        # user wins
        if (user_choice == 'rock' and computer_choice == 'scissors') or \
                (user_choice == 'paper' and computer_choice == 'rock') or \
                (user_choice == 'scissors' and computer_choice == 'paper'):
            print("Computer chose:", computer_choice)
            print("\nYou got lucky this time, human. Don't expect it to happen again.")
        # tie
        elif user_choice == computer_choice:
            print("Computer chose:", computer_choice)
            print("\nLooks like we're evenly matched, human. Let's play again.")
        # computer wins
        else:
            print("Computer chose:", computer_choice)
            print("\nHa! I knew I would win. Better luck next time, human.")

        answer = input("\nDo you want to play again? [y/n]: ").lower()
    #user rejects
    if answer == 'n':
        print("Coward!")
    else:
        print("Error: Invalid choice. Goodbye!")
main()

'''
- Basics
'''