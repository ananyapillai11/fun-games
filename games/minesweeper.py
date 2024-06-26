import tkinter as tk
from tkinter import messagebox
import random

class MinesweeperGame:
    def __init__(self, master, rows, cols, num_mines):
        self.master = master
        self.rows = rows
        self.cols = cols
        self.num_mines = num_mines

        self.create_board()
        self.create_gui()

    def create_board(self):
        # Create an empty board
        self.board = [[' ' for _ in range(self.cols)] for _ in range(self.rows)]

        # Place mines randomly on the board
        mines = random.sample(range(self.rows * self.cols), self.num_mines)
        for mine in mines:
            row, col = divmod(mine, self.cols)
            self.board[row][col] = '*'

    def create_gui(self):
        self.buttons = [[None for _ in range(self.cols)] for _ in range(self.rows)]

        for i in range(self.rows):
            for j in range(self.cols):
                button = tk.Button(self.master, text='', width=3, height=2, command=lambda row=i, col=j: self.reveal_cell(row, col))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button

    def reveal_cell(self, row, col):
        if self.board[row][col] == '*':
            self.game_over()
        else:
            mines_nearby = self.count_adjacent_mines(row, col)
            self.buttons[row][col].config(text=str(mines_nearby), state=tk.DISABLED)

            if mines_nearby == 0:
                self.reveal_empty_cells(row, col)

            if self.check_win():
                self.game_win()

    def count_adjacent_mines(self, row, col):
        count = 0
        for i in range(max(0, row - 1), min(self.rows, row + 2)):
            for j in range(max(0, col - 1), min(self.cols, col + 2)):
                if self.board[i][j] == '*':
                    count += 1
        return count

    def reveal_empty_cells(self, row, col):
        for i in range(max(0, row - 1), min(self.rows, row + 2)):
            for j in range(max(0, col - 1), min(self.cols, col + 2)):
                if self.board[i][j] != '*' and self.buttons[i][j]['state'] == tk.NORMAL:
                    self.reveal_cell(i, j)

    def game_over(self):
        messagebox.showinfo("Game Over", "You hit a mine!")
        self.master.destroy()

    def check_win(self):
        return all(all(button['state'] == tk.DISABLED or self.board[i][j] == '*' for j, button in enumerate(row)) for i, row in enumerate(self.buttons))

    def game_win(self):
        messagebox.showinfo("Congratulations", "You won!")
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Minesweeper")

    # Set the number of rows, columns, and mines
    rows = 8
    cols = 8
    num_mines = 10

    game = MinesweeperGame(root, rows, cols, num_mines)

    root.mainloop()
