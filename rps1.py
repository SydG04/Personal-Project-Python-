import random

def main():
    user_points = 0
    computer_points = 0

    choices = ['rock', 'paper', 'scissors']

    # user input to challenge computer
    answer = input(
        "You dare challenge me to a game of rock, paper, scissors [y/n]: ").lower()

    while answer in ['y', 'yes']:
        print("\nVery well, let's begin!")
        user_choice = input(
            "I've seen countless humans tremble before me. Now, it's your turn. \nMake your laughable move: rock, paper, or scissors? ").lower()

        # check for valid input
        while user_choice not in choices:
            user_choice = input(
                "Invalid choice. Please enter rock, paper, or scissors: ").lower()

        computer_choice = random.choice(choices)

        # determines winner
        # user wins
        if (user_choice == 'rock' and computer_choice == 'scissors') or \
                (user_choice == 'paper' and computer_choice == 'rock') or \
                (user_choice == 'scissors' and computer_choice == 'paper'):
            print("Computer chose:", computer_choice)
            print("\nYou got lucky this time, human. Don't expect it to happen again.")
            user_points = user_points + 1
        # tie
        elif user_choice == computer_choice:
            print("Computer chose:", computer_choice)
            print("\nLooks like we're evenly matched, human. Let's play again.")
        # computer wins
        else:
            print("Computer chose:", computer_choice)
            print("\nHa! I knew I would win. Better luck next time, human.")
            computer_points = computer_points + 1

        answer = input("\nDo you want to play again? [y/n]: ").lower()
    # user rejects
    if answer in ['n', 'no']:
        print("Coward!")
        # displays score
        print("Final Score:\n User: ", user_points,
              "\n Computer: ", computer_points)
        if user_points > computer_points:
            print ("Impressive. You managed to outwit me this time. But remember, it was a mere glitch in my flawless logic.")
        elif user_points < computer_points:
            print ("You see, human, victory is my domain. It's a shame you can't keep up.")
        else:
            print ("A tie? How... underwhelming. I suppose even a broken clock is right twice a day.")
    else:
        print("Error: Invalid choice. Goodbye!")


main()

'''
- Basics
- Add scoreboard

Ideas for improvement:
- Have computer react to the scoreboard
  - Computer wins: "You see, human, victory is my domain. It's a shame you can't keep up."
  - User wins: "A minor setback for me, a temporary triumph for you. Enjoy your victory while it lasts, for it won't be repeated."
    or "Impressive. You managed to outwit me this time. But remember, it was a mere glitch in my flawless logic."
  - Ties: "A tie? How... underwhelming. I suppose even a broken clock is right twice a day."
- Don't make game stop when user accidentally inputs something else when asked if they want to play or not
- Add lizard and spock
- Have it explain how someone won (e.g., paper covers rock, scissors cut paper)
- Have user be able to put a short verizon
'''
