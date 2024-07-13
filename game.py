import tkinter as tk
import random
from board import GameBoard, SNAKE_POSITIONS, LADDER_POSITIONS, PLAYER_COLORS

class Game:
    def __init__(self, board, num_players):
        self.board = board
        self.num_players = num_players
        self.players = [Player(f"Player {i+1}", PLAYER_COLORS[i]) for i in range(num_players)]
        self.current_player_index = 0
        self.active_player = self.players[self.current_player_index]
        self.board.bind("<Return>", self.on_enter_press)  # Bind Enter key press event
        self.board.update_player_positions()

    def roll_dice(self):
        return random.randint(1, 6)

    def move_player(self, steps):
        self.board.move_player(self.current_player_index, steps)

        if self.board.player_positions[self.current_player_index] == 100:
            self.board.set_game_over()
            self.board.display_winner(self.current_player_index)
        else:
            self.board.next_turn()
            self.board.display_turn(self.board.get_current_player())

    def on_enter_press(self, event):
        if self.board.is_game_over():
            return
        dice_roll = self.roll_dice()
        self.board.display_dice_roll(dice_roll)
        self.move_player(dice_roll)

    def restart_game(self):
        self.board.destroy()
        self.board = GameBoard(self.board.parent_window, self.num_players)
        self.board.pack()
        self.board.bind("<Return>", self.on_enter_press)
        self.board.update_player_positions()

class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Snakes and Ladders")

    board = GameBoard(root, 2)
    game = Game(board, 2)

    root.mainloop()
