import random
import tkinter as tk

class SnakeNLadder:
    def __init__(self, master):
        self.master = master
        self.master.title("Snake and Ladder")
        self.canvas = tk.Canvas(self.master, width=600, height=600)
        self.canvas.pack()
        self.draw_board()
        self.create_players()
        self.players_names = ["Player 1", "Player 2"]
        self.current_player = 0
        self.snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
        self.ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
        self.create_dice()
    
    def draw_board(self):
        size = 60
        colors = ['white', 'lightblue']
        for row in range(10):
            for col in range(10):
                x1 = col * size
                y1 = row * size
                x2 = x1 + size
                y2 = y1 + size
                color = colors[(row + col) % 2]
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)
        
        for i in range(1, 101):
            col = (i-1) % 10 if (i-1) // 10 % 2 == 0 else 9 - (i-1) % 10
            row = 9 - (i-1) // 10
            x = col * size + size // 2
            y = row * size + size // 2
            self.canvas.create_text(x, y, text=str(i))

    def create_players(self):
        self.players = [
            self.canvas.create_oval(5, 5, 25, 25, fill='red'),
            self.canvas.create_oval(35, 5, 55, 25, fill='blue')
        ]
        self.positions = [1, 1]

    def create_dice(self):
        self.dice_label = tk.Label(self.master, text="Roll the dice", font=("Arial", 16))
        self.dice_label.pack(pady=20)
        self.roll_button = tk.Button(self.master, text="Roll", command=self.roll_dice)
        self.roll_button.pack(pady=10)
        self.turn_label = tk.Label(self.master, text=f"{self.players_names[self.current_player]}'s turn", font=("Arial", 16))
        self.turn_label.pack(pady=10)

    def roll_dice(self):
        dice_roll = random.randint(1, 6)
        self.dice_label.config(text=f"Dice: {dice_roll}")
        self.move_player(dice_roll)
    
    def move_player(self, steps):
        current_player = self.current_player
        new_position = self.positions[current_player] + steps
        if new_position > 100:
            new_position = 100
        if new_position in self.snakes:
            new_position = self.snakes[new_position]
        elif new_position in self.ladders:
            new_position = self.ladders[new_position]
        self.positions[current_player] = new_position
        self.update_player_position(current_player)
        if new_position == 100:
            self.turn_label.config(text=f"{self.players_names[current_player]} wins!")
            self.roll_button.config(state=tk.DISABLED)
        else:
            self.current_player = (self.current_player + 1) % len(self.players)
            self.turn_label.config(text=f"{self.players_names[self.current_player]}'s turn")

    def update_player_position(self, player):
        pos = self.positions[player]
        col = (pos-1) % 10 if (pos-1) // 10 % 2 == 0 else 9 - (pos-1) % 10
        row = 9 - (pos-1) // 10
        x = col * 60 + 30
        y = row * 60 + 30
        self.canvas.coords(self.players[player], x-10, y-10, x+10, y+10)

if __name__ == "__main__":
    root = tk.Tk()
    app = SnakeNLadder(root)
    root.mainloop()
