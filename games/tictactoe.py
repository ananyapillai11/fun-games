import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")

        self.current_player = "X"
        self.board = [""] * 9

        self.buttons = []
        for i in range(9):
            row, col = divmod(i, 3)
            button = tk.Button(self.root, text="", font=("Helvetica", 24), width=10, height=3,
                               command=lambda idx=i: self.on_button_click(idx))
            button.grid(row=row, column=col, padx=5, pady=5)
            self.buttons.append(button)

    def on_button_click(self, idx):
        if self.board[idx] == "":
            self.board[idx] = self.current_player
            self.buttons[idx].config(text=self.current_player, state="disabled", bg=self.get_player_color())
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
            elif "" not in self.board:
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
            else:
                self.current_player = "X" if self.current_player == "O" else "O"

    def get_player_color(self):
        return "red" if self.current_player == "X" else "blue"

    def check_winner(self):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                          (0, 3, 6), (1, 4, 7), (2, 5, 8),
                          (0, 4, 8), (2, 4, 6)]

        for condition in win_conditions:
            if (self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]]) and \
               (self.board[condition[0]] != ""):
                return True
        return False

    def reset_game(self):
        for i in range(9):
            self.board[i] = ""
            self.buttons[i].config(text="", state="normal", bg="SystemButtonFace")
        self.current_player = "X"

    def start(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.start()
