import tkinter as tk

BOARD_SIZE = 10
CELL_SIZE = 60
SNAKE_POSITIONS = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
LADDER_POSITIONS = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
PLAYER_COLORS = ['blue', 'red', 'green', 'yellow']

class GameBoard(tk.Frame):
    def __init__(self, parent, num_players):
        super().__init__(parent)
        self.parent_window = parent
        self.num_players = num_players
        self.player_positions = [1] * num_players
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

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Snakes and Ladders")

    board = GameBoard(root, 2)
    board.pack()

    root.mainloop()
