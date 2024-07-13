import tkinter as tk
import random

BOARD_SIZE = 10
SNAKE_POSITIONS = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
LADDER_POSITIONS = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
PLAYER_COLORS = ['blue', 'red', 'green', 'yellow']

class GameBoard(tk.Frame):
    def __init__(self, parent, num_players):
        super().__init__(parent)
        self.parent_window = parent
        self.num_players = num_players
        self.player_positions = [1] * num_players
        self.current_player = 0
        self.game_over = False
        self.create_board()

    def create_board(self):
        self.cells = []
        self.cell_widgets = {}
        for row in range(BOARD_SIZE):
            row_cells = []
            for col in range(BOARD_SIZE):
                cell_number = self.calculate_cell_number(row, col)
                cell = tk.Label(self, text=str(cell_number), borderwidth=1, relief="solid", width=6, height=3, bg=self.determine_cell_color(cell_number))
                cell.grid(row=row, column=col)
                row_cells.append(cell)
                self.cell_widgets[cell_number] = cell
            self.cells.append(row_cells)
        self.place_snakes_and_ladders()

    def calculate_cell_number(self, row, col):
        if row % 2 == 0:
            return BOARD_SIZE * (BOARD_SIZE - row) - col
        else:
            return BOARD_SIZE * (BOARD_SIZE - row - 1) + col + 1

    def determine_cell_color(self, cell_number):
        if cell_number in SNAKE_POSITIONS:
            return 'lightcoral'
        elif cell_number in LADDER_POSITIONS:
            return 'lightgreen'
        else:
            return 'white'

    def place_snakes_and_ladders(self):
        for start, end in SNAKE_POSITIONS.items():
            self.cell_widgets[start].config(bg='red', text=f'{start} -> {end}')
        for start, end in LADDER_POSITIONS.items():
            self.cell_widgets[start].config(bg='green', text=f'{start} -> {end}')

    def move_player(self, player_index, steps):
        current_position = self.player_positions[player_index]
        new_position = current_position + steps
        if new_position > 100:
            new_position = 100 - (new_position - 100)
        self.player_positions[player_index] = new_position
        self.check_snake_or_ladder(player_index, new_position)
        self.update_player_positions()

    def check_snake_or_ladder(self, player_index, position):
        if position in SNAKE_POSITIONS:
            new_position = SNAKE_POSITIONS[position]
            self.player_positions[player_index] = new_position
        elif position in LADDER_POSITIONS:
            new_position = LADDER_POSITIONS[position]
            self.player_positions[player_index] = new_position

    def roll_dice(self):
        return random.randint(1, 6)

    def next_turn(self):
        self.current_player = (self.current_player + 1) % self.num_players

    def get_current_player(self):
        return self.current_player

    def is_game_over(self):
        return self.game_over

    def set_game_over(self, value=True):
        self.game_over = value

    def display_turn(self, player_index):
        print(f"Player {player_index + 1}'s turn")

    def display_dice_roll(self, dice_roll):
        print(f"Dice rolled: {dice_roll}")

    def display_winner(self, player_index):
        print(f"Player {player_index + 1} wins!")

    def update_player_positions(self):
        for i in range(self.num_players):
            position = self.player_positions[i]
            self.cell_widgets[position].config(text=f"Player {i + 1}")

    def restart_game(self):
        self.destroy()
        self.__init__(self.parent_window, self.num_players)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Snakes and Ladders")
    board = GameBoard(root, 2)
    board.pack()
    root.mainloop()
