import tkinter as tk
import random


# Function to determine the outcome of the game
def play_game(user_choice):
    computer_choice = random.choice([1, 2, 3])
    choices = {1: "stone", 2: "paper", 3: "scissor"}

    computer_choice_str = choices[computer_choice]
    user_choice_str = choices[user_choice]

    result_text.set(f"{user_name.get()} chose {user_choice_str},\nComputer chose {computer_choice_str}.")

    if user_choice == computer_choice:
        result_text.set(result_text.get() + "\nThe match is Draw.")
    elif (user_choice == 1 and computer_choice == 2) or \
         (user_choice == 2 and computer_choice == 3) or \
         (user_choice == 3 and computer_choice == 1):
        result_text.set(result_text.get() + f"\n{user_name.get()} lost the game.")
    else:
        result_text.set(result_text.get() + f"\n{user_name.get()} won the game.")

# Setting up the main application window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

# User name input
tk.Label(root, text="Enter your name:").pack()
user_name = tk.StringVar()
tk.Entry(root, textvariable=user_name).pack()

# Choice buttons
tk.Label(root, text="Choose one:").pack()
tk.Button(root, text="Stone", command=lambda: play_game(1)).pack()
tk.Button(root, text="Paper", command=lambda: play_game(2)).pack()
tk.Button(root, text="Scissor", command=lambda: play_game(3)).pack()

# Result display
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, wraplength=250)
result_label.pack()

# Start the application
root.mainloop()
