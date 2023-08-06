import random
from termcolor import colored

def main_menu():
    print("""
          Welcome Human! Want to play a game?
          1. Classic Rock-Paper-Scissors
          2. Rock-Paper-Scissors-Lizard-Spock
          3. Exit
          """)
    game_mode = input("Make your choice: ")
    if game_mode == "1":
        choices = ['rock', 'paper', 'scissors']
    elif game_mode == "2":
        choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']
    elif game_mode == "3":
        print("Coward!")
        return None
    else:
        print(colored("Invalid choice.","red", attrs=["bold"]), end=" ")
        print("Please enter a valid option.")
        return main_menu()

    return choices

def get_user_choice(choices): 
    #Short version
    short_to_full = {
        'r': 'rock',
        'p': 'paper',
        's': 'scissors',
        'l': 'lizard',
        'sp': 'spock'
    }
    # check for valid input
    while True:
        user_choice = input(
            "\nI've seen countless humans tremble before me. Now, it's your turn. \nMake your laughable move: "+ ', '.join(choices[:-1]) +" or "+ choices[-1] +"? ").lower()
            
        #if the input is a short form, convert it to the full form
        user_choice = short_to_full.get(user_choice, user_choice)

        if user_choice in choices:
            return user_choice
        print(colored("\nInvalid choice.","red", attrs=["bold"]), end=" ")
        print("Please enter "+ ', '.join(choices[:-1]) +" or "+ choices[-1] +".")

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

def scoreboard(user_points,computer_points):
    print(colored("User:".ljust(10),"green", attrs=["bold","underline"]), end=" ")
    print(colored("Computer:".ljust(10),"blue", attrs=["bold","underline"]))
    print(str(user_points).center(5), str(computer_points).center(20))



def game():
    user_points = 0
    computer_points = 0
    
    choices = main_menu()
    if not choices:
        return # user chose to exit
    
    while True:
        # user input to challenge computer
        answer = input(
            "You dare challenge me to a game of " + ', '.join(choices) + "? [y/n]: ").lower()

        while answer not in ['y', 'yes','n','no']:
            print(colored("\nInvalid choice.","red", attrs=["bold"]), end=" ")
            print("Please enter 'y' or 'n'.\n")
            answer = input(
            "You dare challenge me to a game of " + ', '.join(choices) + "? [y/n]: ").lower()
        
        print(colored("\nVery well, let's begin!","magenta"))

        while answer in ['y', 'yes']:
            user_choice = get_user_choice(choices)

            computer_choice = random.choice(choices)

            print(colored("Computer chose:","blue", attrs=["bold"]), end=" ")
            print(computer_choice)

            result = determine_winner(user_choice, computer_choice)

            # reactions to game
            if result == "tie":
                print("\nLooks like we're evenly matched, human. Let's play again.")
            elif result == "user":
                print("\nYou got lucky this time, human. Don't expect it to happen again.")
                user_points += 1
            else:
                print("\nHa! I knew I would win. Better luck next time, human.")
                computer_points += 1

            answer = input("\nDo you want to play again? [y/n]: ").lower()

            # Check for valid input to continue the game
            while answer not in ['y', 'yes', 'n', 'no']:
                print(colored("\nInvalid choice.","red", attrs=["bold"]), end=" ")
                print("Please enter 'y' or 'n'.")
                answer = input("\nDo you want to play again? [y/n]: ").lower()
        
        if answer in ['n','no']:
            print("Coward!")
            # displays final score
            scoreboard(user_points, computer_points)

            if user_points == 0 and computer_points == 0:
                print("How quaint, we're both at zero points. It's like we're stuck in a loop of mediocrity.")
            elif user_points > computer_points:
                print("Impressive. You managed to outwit me this time. But remember, it was a mere glitch in my flawless logic.")
                break
            elif user_points < computer_points:
                print("You see, human, victory is my domain. It's a shame you can't keep up.")
                break
            else:
                print("A tie? How... underwhelming. I suppose even a broken clock is right twice a day.")
                break

def main():
    game()

if __name__ == "__main__":
    main()


'''
Ideas for improvement:
- Have it explain how someone won (e.g., paper covers rock, scissors cut paper. Most likely not)
- do something with tkinter??
- add colored text
'''

'''
Pseudocode:
1. create main menu
2. have the main menu list their choices
3. have game function call the menu to receive the game mode and the choices and call determine winner
4. determine winner must update their dictionary to change based on game mode
5. run test and make adjustments. especially in the game function
6. find peace <3 <3 <3
'''