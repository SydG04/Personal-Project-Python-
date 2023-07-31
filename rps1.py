import random

def get_user_choice():    
    choices = ['rock', 'paper', 'scissors', 'lizard','spock']
    # check for valid input
    while True:
        user_choice = input(
            "I've seen countless humans tremble before me. Now, it's your turn. \nMake your laughable move: rock, paper, scissors, lizard, or spock? ").lower()
        if user_choice in choices:
            return user_choice
        print("Invalid choice. Please enter rock, paper, scissors, lizard, or spock.")

def determine_winner(user_choice, computer_choice):
    outcomes = {
        'rock': ['scissors', 'lizard'],
        'paper': ['rock', 'spock'],
        'scissors': ['paper', 'lizard'],
        'lizard': ['paper', 'spock'],
        'spock': ['rock', 'scissors']
    }
    #tie
    if user_choice == computer_choice:
        return "tie"
    #user wins
    elif computer_choice in outcomes[user_choice]:
        return "user"
    #computer wins
    else: 
        return "computer"

def game():
    user_points = 0
    computer_points = 0
    
        # user input to challenge computer
    answer = input(
        "You dare challenge me to a game of rock, paper, scissors, lizard, or spock [y/n]: ").lower()

    # initial message outside the while loop
    print("\nVery well, let's begin!")

    while answer in ['y', 'yes']:
        user_choice = get_user_choice()

        computer_choice = random.choice(['rock', 'paper', 'scissors', 'lizard', 'spock'])

        print("Computer chose:", computer_choice)

        result = determine_winner(user_choice, computer_choice)
        
        #reactions to game
        if result == "tie":
            print("\nLooks like we're evenly matched, human. Let's play again.")
        elif result == "user":
            print("\nYou got lucky this time, human. Don't expect it to happen again.")
            user_points += 1
        else:
            print("\nHa! I knew I would win. Better luck next time, human.")
            computer_points += 1

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


def main():
    game()

if __name__ == "__main__":
    main()


'''
- Basics
- Add scoreboard

Ideas for improvement:
- Don't make game stop when user accidentally inputs something else when asked if they want to play or not
- Have it explain how someone won (e.g., paper covers rock, scissors cut paper)
- Have user be able to put a short verizon
- Make a version where people can choose to play simple rps or rpslsp
'''
