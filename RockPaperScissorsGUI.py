import tkinter as tk
import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

def play_game(user_choice):
    global user_wins, computer_wins
    computer_choice = random.choice(options)

    computer_pick_label.config(text=f"Computer Picked {computer_choice.capitalize()}.")

    if user_choice == computer_choice:
        result_label.config(text="It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        result_label.config(text="You won!")
        user_wins += 1
    else:
        result_label.config(text="You Lost!")
        computer_wins += 1

    score_label.config(text=f"You: {user_wins} | Computer: {computer_wins}")

def refresh_game():
    global user_wins, computer_wins
    user_wins = 0
    computer_wins = 0
    score_label.config(text="You: 0 | Computer: 0")
    result_label.config(text="")
    computer_pick_label.config(text="")

# Create Tkinter window
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")
root.geometry("400x300")
root.configure(bg="#d3d3d3")  # Set background color to gray

# Create GUI components
computer_pick_label = tk.Label(root, text="", bg="#d3d3d3")
computer_pick_label.pack()

rock_button = tk.Button(root, text="Rock", command=lambda: play_game("rock"), bg="#d3d3d3")
rock_button.pack(side=tk.LEFT, padx=10)

paper_button = tk.Button(root, text="Paper", command=lambda: play_game("paper"), bg="#d3d3d3")
paper_button.pack(side=tk.LEFT, padx=10)

scissors_button = tk.Button(root, text="Scissors", command=lambda: play_game("scissors"), bg="#d3d3d3")
scissors_button.pack(side=tk.LEFT, padx=10)

refresh_button = tk.Button(root, text="Refresh", command=refresh_game, bg="#d3d3d3")
refresh_button.pack(pady=10)

result_label = tk.Label(root, text="", bg="#d3d3d3")
result_label.pack()

score_label = tk.Label(root, text="You: 0 | Computer: 0", bg="#d3d3d3")
score_label.pack()

# Run the Tkinter event loop
root.mainloop()