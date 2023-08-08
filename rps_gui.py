import random
from tkinter import *
from tkinter import messagebox

# create object
root = Tk()

# set
root.geometry("300x250")

# title
root.title("Rock Paper Scissors")


def main_menu():
    menu = Label(root, text=""" 
        Welcome Human! Want to play a game?
          1. Classic Rock-Paper-Scissors
          2. Rock-Paper-Scissors-Lizard-Spock
          3. Exit
        """)
    menu.pack(pady=(10, 0), padx=(0, 10))

    def start_classic_rps():
        challenge_message = messagebox.askyesno(
            "Game Challenge", "You dare challenge me to a game of rock, paper, scissors?")

        if challenge_message:
            messagebox.showinfo("Game challenge", "Very well, let's begin!")
            root.destroy()  # close the current window
            game_root = Tk()  # open a new window for the classic RPS
            choices = ['rock', 'paper', 'scissors']
            game_mode = "Classic RPS"
            game(choices, game_mode, game_root)

        else:
            messagebox.showwarning(
                "Warning", "Choosing is simple, yet you struggle. Perhaps you're not cut out for this.")

    def start_rpslsp():
        challenge_message = messagebox.askyesno(
            "Game Challenge", "You dare challenge me to a game of rock, paper, scissors, lizard, spock?")

        if challenge_message:
            messagebox.showinfo("Game challenge", "Very well, let's begin!")
            root.destroy()  # close the current window
            game_root = Tk()  # open a new window for the RPSLSP
            choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']
            game_mode = "RPSLSP"
            game(choices, game_mode, game_root)

        else:
            messagebox.showwarning(
                "Warning", "Choosing is simple, yet you struggle. Perhaps you're not cut out for this.")

    def exit_game():
        confirm_exit = messagebox.askyesno(
            "Confirm Exit", "Are you too scared to challenge me?")

        if confirm_exit:
            messagebox.showinfo("Exit Message", "Coward!")
            root.destroy()

        else:
            messagebox.showinfo(
                "Confirm Exit", "Couldn't resist a challenge, I see.")


# Create a Frame to center the buttons horizontally
    global frame
    frame = Frame(root)
    # Add vertical padding to center the buttons vertically
    frame.pack(pady=50)


# Button creation
    btn_classic_rps = Button(frame, text="Classic RPS",
                             command=start_classic_rps)
    btn_classic_rps.pack(side=LEFT, padx=20, pady=10, expand=True, fill=BOTH)
    # Use expand and fill options to center the button horizontally

    btn_rpslsp = Button(frame, text="RPSLSP", command=start_rpslsp)
    btn_rpslsp.pack(side=LEFT, padx=20, pady=10, expand=True, fill=BOTH)

    btn_exit = Button(frame, text="Exit", command=exit_game)
    btn_exit.pack(side=LEFT, padx=20, pady=10, expand=True, fill=BOTH)

def determine_winner(user_choice, computer_choice):
    outcomes = {
        'rock': ['scissors', 'lizard'],
        'paper': ['rock', 'spock'],
        'scissors': ['paper', 'lizard'],
        'lizard': ['paper', 'spock'],
        'spock': ['rock', 'scissors']
    }

    if user_choice == computer_choice:
        return "It's a tie!"
    elif computer_choice in outcomes[user_choice]:
        return "You win!"
    else: 
        return "I win!"


def game(choices, game_mode, game_root):
    user_points = 0 
    computer_points = 0
    
    game_root.title(f"{game_mode}")

    # Geometry changes depending on game mode
    if game_mode == "Classic RPS":
        game_root.geometry("400x300")
    else:
        game_root.geometry("400x250")

    # Create a Frame to center the buttons horizontally
    frame1 = Frame(game_root)
    # Add vertical padding to center the buttons vertically
    frame1.pack(pady=50)

    # Create labels to display available choices
    choices_label = Label(frame1, text="I've seen countless humans tremble before me. Now, it's your turn. \nMake your laughable move: "+ ', '.join(choices[:-1]) +" or "+ choices[-1] +"? ")
    choices_label.pack()

    for choice in choices:
        choices_btns = Button(frame1, text=choice.capitalize())
        choices_btns.pack(side=LEFT, padx=10, pady=10, expand=True, fill=BOTH)




def main():
    main_menu()

    # Execute Tkinter
    root.mainloop()


main()


'''
Ideas for improvement:
- Have it explain how someone won (e.g., paper covers rock, scissors cut paper)
- do something with tkinter??
'''

'''
Pseudocode:
1. create main menu
2. have the main menu list their choices
3. have game function call the menu to receive the game mode and the choices and call determine winner
4. determine winner must update their dictionary to change based on game mode
10. run test and make adjustments. especially in the game function
6. find peace <3 <3 <3
'''
