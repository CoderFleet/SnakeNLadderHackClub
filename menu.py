import tkinter as tk
from board import GameBoard
from game import Game

class PlayerMenu(tk.Menu):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent_window = parent

        self.add_command(label="2 Players", command=lambda: self.start_game(2))
        self.add_command(label="3 Players", command=lambda: self.start_game(3))
        self.add_command(label="4 Players", command=lambda: self.start_game(4))
        self.add_separator()
        self.add_command(label="Exit", command=self.parent_window.quit)

    def start_game(self, num_players):
        if hasattr(self.parent_window, 'board'):
            self.parent_window.board.destroy()

        game_board = GameBoard(self.parent_window, num_players)
        game_board.pack()

        self.parent_window.board = game_board

        game = Game(game_board, num_players)
        game.start()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Snakes and Ladders")

    menu = PlayerMenu(root)
    root.config(menu=menu)

    root.mainloop()
