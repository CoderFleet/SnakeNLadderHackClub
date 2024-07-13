import tkinter as tk
from board import GameBoard
from game import Game
from menu import PlayerMenu

class SnakesAndLaddersApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Snakes and Ladders")

        self.setup_menu()

    def setup_menu(self):
        self.menu_bar = tk.Menu(self)

        # Initialize the player menu
        self.player_menu = PlayerMenu(self)
        self.menu_bar.add_cascade(label="Menu", menu=self.player_menu)

        self.config(menu=self.menu_bar)

    def start_game(self, num_players):
        if hasattr(self, 'board'):
            self.board.destroy()

        self.board = GameBoard(self, num_players)
        self.board.pack()

        self.game = Game(self.board, num_players)
        self.game.start()

if __name__ == "__main__":
    app = SnakesAndLaddersApp()
    app.mainloop()
