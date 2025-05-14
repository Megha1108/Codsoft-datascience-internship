#RockPaperScissor

import tkinter as tk
from tkinter import ttk, messagebox
import random

class RockPaperScissorGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Rock Paper Scissor")
        self.master.geometry("700x400")
        self.master.configure(bg="#000000")

        self.user_score = 0
        self.computer_score = 0

        self.style = ttk.Style()
        self.style.configure("TFrame", background="#000000")
        self.style.configure("TLabel", background="#000000", foreground="#ffffff", font=("Helvetica", 17, "bold"))
        self.style.configure("TButton", background="#2ecc71", font=("Helvetica", 12, "bold"))

        self.frame = ttk.Frame(master)
        self.frame.grid(row=0, column=0, pady=20)

        self.user_choice_label = ttk.Label(self.frame, text="your choice")
        self.user_choice_label.grid(row=0, column=0, padx=20, pady=20)

        self.user_choice_var = tk.StringVar()
        self.user_choice_entry = ttk.Combobox(self.frame, textvariable= self.user_choice_var, values=["Rock", "Paper", "Scissor"])
        self.user_choice_entry.grid(row=0, column=1, padx=20, pady=20)
        self.user_choice_entry.current(0)

        self.choose_button = ttk.Button(self.frame, text="choose", command=self.play_round)
        self.choose_button.grid(row=0, column=2, padx=20, pady=20)

        self.result_label = ttk.Label(self.frame, text=" ", foreground="#e74c3c")
        self.result_label.grid(row=1, column=1, padx=20, pady=20)

        self.score_label = ttk.Label(self.frame, text="score - you: 0| Computer: 0",foreground="#2c3e50")
        self.score_label.grid(row=2, column=1, padx=10, pady=10)

        self.play_again_button = ttk.Button(self.frame, text="play again", command=self.reset_game)
        self.play_again_button.grid(row=3, column=1, padx=20, pady=20)
        self.play_again_button.grid_remove()

    def get_computer_choice(self):
        return random.choice(["Rock", "Paper", "Scissor"])

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "it's a tie"
        elif(
            (user_choice == "Rock" and computer_choice == "Scissor") or
            (user_choice == "Scissor" and computer_choice == "Paper") or
            (user_choice == "Paper" and computer_choice == "Rock")
        ):
            self.user_score += 1
            return "you win!"
        else:
            self.computer_score += 1
            return "you lose"

    def display_result(self, user_choice, computer_choice, result):
        self.result_label.config(text=f"{result}\nYour choice: {user_choice}\nComputer's choice: {computer_choice}")

        if "win" in result:
            self.result_label.configure(foreground="#2ecc71")
        elif "lose" in result:
            self.result_label.configure(foreground="#e74c3c")

        self.score_label.config(text=f"score - you: {self.user_score} | computer: {self.computer_score}")

    def play_round(self):
        user_choice = self.user_choice_var.get()
        computer_choice = self.get_computer_choice()
        result = self.determine_winner(user_choice, computer_choice)
        self.display_result(user_choice, computer_choice, result)

        if self.user_score == 3 or self.computer_score == 3:
            self.show_game_over()

    def reset_game(self):
        self.user_score = 0
        self.computer_score = 0
        self.result_label.config(text="", foreground="#e74c3c")
        self.score_label.config(text="score - you: 0 | computer: 0", foreground="#2c3e50")
        self.play_again_button.grid_remove()

    def show_game_over(self):
        if self.user_score == 3:
            message = "Congratulations! You won the game."
        else:
            message = "You lose."

        messagebox.showinfo("Game Over", message)
        self.reset_game()

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorGame(root)
    root.mainloop()
