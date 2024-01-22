import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Rock-Paper-Scissors Game")

        self.user_score = 0
        self.computer_score = 0

        self.label = tk.Label(master, text="Choose rock, paper, or scissors:")
        self.label.pack()

        self.buttons_frame = tk.Frame(master)
        self.buttons_frame.pack()

        self.rock_button = tk.Button(self.buttons_frame, text="Rock", command=lambda: self.play_round("rock"))
        self.rock_button.grid(row=0, column=0, padx=10)

        self.paper_button = tk.Button(self.buttons_frame, text="Paper", command=lambda: self.play_round("paper"))
        self.paper_button.grid(row=0, column=1, padx=10)

        self.scissors_button = tk.Button(self.buttons_frame, text="Scissors", command=lambda: self.play_round("scissors"))
        self.scissors_button.grid(row=0, column=2, padx=10)

        self.score_label = tk.Label(master, text="Score - You: 0, Computer: 0")
        self.score_label.pack()

    def play_round(self, user_choice):
        computer_choice = random.choice(['rock', 'paper', 'scissors'])

        result = self.determine_winner(user_choice, computer_choice)
        self.show_result(user_choice, computer_choice, result)

        if 'win' in result:
            self.user_score += 1
        elif 'lose' in result:
            self.computer_score += 1

        self.update_score_label()

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return 'It\'s a tie!'
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            return 'You win!'
        else:
            return 'You lose!'

    def show_result(self, user_choice, computer_choice, result):
        messagebox.showinfo("Result", f"You chose: {user_choice}\nComputer chose: {computer_choice}\n\n{result}")

    def update_score_label(self):
        self.score_label.config(text=f"Score - You: {self.user_score}, Computer: {self.computer_score}")

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()
