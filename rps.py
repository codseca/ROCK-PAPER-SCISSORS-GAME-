import tkinter as tk
from tkinter import messagebox
import random
import sys

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors")
        
        self.user_score = 0
        self.computer_score = 0
        
        # Set the background color of the root window
        self.root.configure(bg="black")
        
        # Create main frame
        self.main_frame = tk.Frame(self.root, bg="black")
        self.main_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)
        
        # Create buttons for user choices with white text and background
        self.rock_button = tk.Button(self.main_frame, text="Rock", command=lambda: self.play("rock"),
                                     bg="white", fg="black")
        self.paper_button = tk.Button(self.main_frame, text="Paper", command=lambda: self.play("paper"),
                                      bg="white", fg="black")
        self.scissors_button = tk.Button(self.main_frame, text="Scissors", command=lambda: self.play("scissors"),
                                         bg="white", fg="black")
        
        # Layout buttons in the center of the frame
        self.rock_button.grid(row=0, column=0, padx=10, pady=10)
        self.paper_button.grid(row=0, column=1, padx=10, pady=10)
        self.scissors_button.grid(row=0, column=2, padx=10, pady=10)
        
        # Configure grid to center buttons
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=1)
        self.main_frame.grid_columnconfigure(2, weight=1)
        
        # Create scoreboard frame with black background
        self.scoreboard_frame = tk.Frame(self.root, bg="black")
        self.scoreboard_frame.pack(side=tk.RIGHT, padx=20, pady=20, fill=tk.Y)
        
        self.user_score_label = tk.Label(self.scoreboard_frame, text="Your Score: 0", font=("Arial", 14),
                                         bg="black", fg="white")
        self.user_score_label.pack()
        
        self.computer_score_label = tk.Label(self.scoreboard_frame, text="Computer Score: 0", font=("Arial", 14),
                                             bg="black", fg="white")
        self.computer_score_label.pack()
        
        self.result_label = tk.Label(self.main_frame, text="", font=("Arial", 16), bg="black", fg="white")
        self.result_label.grid(row=1, column=0, columnspan=3, pady=10)
        
        # Tooltips
        self.add_tooltip(self.rock_button, "Choose Rock to crush Scissors")
        self.add_tooltip(self.paper_button, "Choose Paper to cover Rock")
        self.add_tooltip(self.scissors_button, "Choose Scissors to cut Paper")
    
    def add_tooltip(self, widget, text):
        tooltip = tk.Label(self.root, text=text, bg="lightyellow", relief="solid", borderwidth=1, padx=5, pady=5)
        
        def on_enter(event):
            x, y, _, _ = widget.bbox("insert")
            x += widget.winfo_rootx() + 25
            y += widget.winfo_rooty() + 25
            tooltip.place(x=x, y=y)
        
        def on_leave(event):
            tooltip.place_forget()
        
        widget.bind("<Enter>", on_enter)
        widget.bind("<Leave>", on_leave)
    
    def get_computer_choice(self):
        choices = ["rock", "paper", "scissors"]
        return random.choice(choices)
    
    def get_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "tie"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            return "win"
        else:
            return "lose"
    
    def play(self, user_choice):
        computer_choice = self.get_computer_choice()
        result = self.get_winner(user_choice, computer_choice)
        
        self.result_label.config(
            text=f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\nResult: {result.capitalize()}"
        )
        
        if result == "win":
            self.user_score += 1
            messagebox.showinfo("Result", "Congratulations! You win!")
        elif result == "lose":
            self.computer_score += 1
            messagebox.showinfo("Result", "Sorry, you lose. Better luck next time!")
        else:
            messagebox.showinfo("Result", "It's a tie!")
        
        self.update_scoreboard()
        self.ask_play_again()
    
    def update_scoreboard(self):
        self.user_score_label.config(text=f"Your Score: {self.user_score}")
        self.computer_score_label.config(text=f"Computer Score: {self.computer_score}")

    def ask_play_again(self):
        response = messagebox.askyesno("Play Again", "Do you want to play another round?")
        if not response:
            self.create_exit_button()

    def create_exit_button(self):
        # Ensure only one exit button is created
        if not hasattr(self, 'exit_button'):
            # Create and place the exit button
            self.exit_button = tk.Button(self.main_frame, text="Exit", command=self.exit_game,
                                         bg="red", fg="white", font=("Arial", 14))
            self.exit_button.grid(row=2, column=0, columnspan=3, pady=20)
    
    def exit_game(self):
        self.root.quit()
        sys.exit()

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()
