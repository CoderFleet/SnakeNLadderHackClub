import tkinter as tk
from board import GameBoard
from game import Game

class PlayerMenu(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent_window = parent
        self.create_widgets()

    def create_widgets(self):
        self.label_select_players = tk.Label(self, text="Select number of players (2-4):", font=("Arial", 16))
        self.label_select_players.pack(pady=20)

        self.player_count = tk.IntVar(value=2)
        for num in range(2, 5):
            rb_player = tk.Radiobutton(self, text=str(num), variable=self.player_count, value=num, font=("Arial", 14))
            rb_player.pack(pady=10)

        self.start_button = tk.Button(self, text="Start Game", command=self.start_game, font=("Arial", 14))
        self.start_button.pack(pady=20)

    def start_game(self):
        num_players = self.player_count.get()
        self.destroy()
        game_board = GameBoard(self.parent_window, num_players)
        game_board.pack()
        game = Game(game_board, num_players)
        game.start()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Snakes and Ladders")

    menu = PlayerMenu(root)
    menu.pack()

    root.mainloop()
