import random

# starting points
user = 0
computer = 0

# the scoreboard


def scoreboard():
    print("User:".ljust(10), "Computer:".ljust(12))
    print("----".ljust(10), "--------".ljust(12))
    print(str(user).center(5), str(computer).center(7))


# options list


def options():
    rock = ['rock', 'r']
    paper = ['paper', 'p']
    scissors = ['scissors', 's']
    return [rock, paper, scissors]


def game():
    # Declare use and computer as global variable
    global user, computer
    ushort = [options()[0][1], options()[1][1], options()[2][1]]
    ufull = [options()[0][0], options()[1][0], options()[2][0]]
    cfull = [options()[0][0], options()[1][0], options()[2][0]]

    # user input to challenge computer
    answer = input(
        "You dare challenge me to a game of rock, paper, scissors [y/n]: ").lower()

    while answer in ['y', 'yes']:
        # the outcome depending on user choice
        if answer in ['y', 'yes']:
            print("\nVery well, lets begin!")
            user_choice = input(
                "Type your choice: rock (r), paper (p), or scissors (s): ").lower()
            computer_choice = random.choice(options())

            # check for valid input
            while user_choice not in [choice for option in options() for choice in option]:
                print("Invalid choice. Please choose rock, paper, or scissors.")
                user_choice = input(
                    "Type your choice: rock (r), paper (p), or scissors (s): ").lower()

        # Check if user's choice is a shortened version
            if user_choice in ushort:
                user_choice_full = ufull[ushort.index(user_choice)]
            else:
                user_choice_full = user_choice

        # determines winner
            # user wins
            if (user_choice_full == 'rock' and computer_choice == 'scissors') or \
               (user_choice_full == 'paper' and computer_choice == 'rock') or \
               (user_choice_full == 'scissors' and computer_choice == 'paper'):
                print("Computer chose:", computer_choice[0],
                      "\n\nYou got lucky this time, human. Don't expect it to happen again.")
                user = user + 1  # user gets a point
            # tie (no points given)
            elif user_choice_full == computer_choice:
                print("Computer chose:", computer_choice,
                      "\n\nLooks like we're evenly matched, human. Let's play again.")
            # computer wins
            else:
                print("Computer chose:", computer_choice,
                      "\n\nHa! I knew I would win. Better luck next time, human.")
                computer = computer + 1  # computer gets a point

      # Ask user if they want to play again
            answer = input("Do you want to play again? [y/n]: ").lower()
        else:
            print("Coward!")
            print("Final Score:")
            # Displays scoreboard :D
            scoreboard()
            break
    else:
        if answer not in ['n', 'no']:
            print("error:invalid choice. Goodbye!")
            print("Final Score:")
            scoreboard()


def main():
    # starts game
    game()


main()
