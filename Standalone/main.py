import random
import tkinter as tk
from tkinter import simpledialog, messagebox


class SnakeNLadder:
    def __init__(self, master):
        self.master = master
        self.master.title("Snake and Ladder")
        self.canvas = tk.Canvas(self.master, width=600, height=600)
        self.canvas.pack()
        self.players_names = ["Player 1", "Player 2"]
        self.current_player = 0
        self.snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
        self.ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
        self.draw_board()
        self.create_players()
        self.create_dice()
        self.dice_animation_speed = 100
        self.roll_in_progress = False
        self.dice_roll = 0
        self.create_reset_button()
        self.create_player_indicators()
        self.create_snake_ladder_display()
        self.create_dice_images()

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
            col = (i - 1) % 10 if (i - 1) // 10 % 2 == 0 else 9 - (i - 1) % 10
            row = 9 - (i - 1) // 10
            x = col * size + size // 2
            y = row * size + size // 2
            self.canvas.create_text(x, y, text=str(i))

        # Draw snakes and ladders on the board
        for start, end in self.snakes.items():
            self.draw_snake(start, end)
        for start, end in self.ladders.items():
            self.draw_ladder(start, end)

    def draw_snake(self, start, end):
        self.draw_arrow(start, end, 'red')

    def draw_ladder(self, start, end):
        self.draw_arrow(start, end, 'green')

    def draw_arrow(self, start, end, color):
        size = 60
        start_col = (start - 1) % 10 if (start - 1) // 10 % 2 == 0 else 9 - (start - 1) % 10
        start_row = 9 - (start - 1) // 10
        end_col = (end - 1) % 10 if (end - 1) // 10 % 2 == 0 else 9 - (end - 1) % 10
        end_row = 9 - (end - 1) // 10

        start_x = start_col * size + size // 2
        start_y = start_row * size + size // 2
        end_x = end_col * size + size // 2
        end_y = end_row * size + size // 2

        self.canvas.create_line(start_x, start_y, end_x, end_y, arrow=tk.LAST, fill=color, width=3)

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
        self.turn_label = tk.Label(self.master, text=f"{self.players_names[self.current_player]}'s turn",
                                   font=("Arial", 16))
        self.turn_label.pack(pady=10)

    def create_reset_button(self):
        self.reset_button = tk.Button(self.master, text="Reset", command=self.reset_game)
        self.reset_button.pack(pady=10)

    def create_player_indicators(self):
        self.player_indicators = [
            tk.Label(self.master, text=f"{self.players_names[0]}: 1", font=("Arial", 12)),
            tk.Label(self.master, text=f"{self.players_names[1]}: 1", font=("Arial", 12))
        ]
        for idx, label in enumerate(self.player_indicators):
            label.pack(pady=5)

    def create_snake_ladder_display(self):
        self.snake_ladder_frame = tk.Frame(self.master)
        self.snake_ladder_frame.pack(pady=20)

        snake_label = tk.Label(self.snake_ladder_frame, text="Snakes:", font=("Arial", 12))
        snake_label.grid(row=0, column=0, padx=10)
        self.snake_listbox = tk.Listbox(self.snake_ladder_frame, height=5, width=15, font=("Arial", 12))
        self.snake_listbox.grid(row=0, column=1, padx=10)
        for key in self.snakes:
            self.snake_listbox.insert(tk.END, f"{key} -> {self.snakes[key]}")

        ladder_label = tk.Label(self.snake_ladder_frame, text="Ladders:", font=("Arial", 12))
        ladder_label.grid(row=1, column=0, padx=10)
        self.ladder_listbox = tk.Listbox(self.snake_ladder_frame, height=5, width=15, font=("Arial", 12))
        self.ladder_listbox.grid(row=1, column=1, padx=10)
        for key in self.ladders:
            self.ladder_listbox.insert(tk.END, f"{key} -> {self.ladders[key]}")

    def create_dice_images(self):
        self.dice_images = [
            tk.PhotoImage(file="dice1.png").subsample(2),
            tk.PhotoImage(file="dice2.png").subsample(2),
            tk.PhotoImage(file="dice3.png").subsample(2),
            tk.PhotoImage(file="dice4.png").subsample(2),
            tk.PhotoImage(file="dice5.png").subsample(2),
            tk.PhotoImage(file="dice6.png").subsample(2)
        ]
        self.dice_image_label = tk.Label(self.master, image=self.dice_images[0])
        self.dice_image_label.pack(pady=10)

    def reset_game(self):
        self.positions = [1, 1]
        self.current_player = 0
        self.update_player_position(0)
        self.update_player_position(1)
        self.turn_label.config(text=f"{self.players_names[self.current_player]}'s turn")
        self.roll_button.config(state=tk.NORMAL)
        for label in self.player_indicators:
            label.config(text=f"{self.players_names[self.player_indicators.index(label)]}: 1")

    def roll_dice(self):
        if not self.roll_in_progress:
            self.roll_in_progress = True
            self.roll_button.config(state=tk.DISABLED)
            self.dice_animation(0)

    def dice_animation(self, frame):
        if frame < 10:
            self.dice_roll = random.randint(1, 6)
            self.dice_label.config(text=f"Dice: {self.dice_roll}")
            self.dice_image_label.config(image=self.dice_images[self.dice_roll - 1])
            frame += 1
            self.master.after(self.dice_animation_speed, self.dice_animation, frame)
        else:
            self.roll_in_progress = False
            self.move_player(self.dice_roll)
            self.roll_button.config(state=tk.NORMAL)

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
        self.update_player_indicator(current_player, new_position)
        if new_position == 100:
            self.turn_label.config(text=f"{self.players_names[current_player]} wins!")
            self.roll_button.config(state=tk.DISABLED)
            messagebox.showinfo("Game Over", f"{self.players_names[current_player]} wins the game!")
        else:
            self.current_player = (self.current_player + 1) % len(self.players)
            self.turn_label.config(text=f"{self.players_names[self.current_player]}'s turn")

    def update_player_position(self, player):
        pos = self.positions[player]
        col = (pos - 1) % 10 if (pos - 1) // 10 % 2 == 0 else 9 - (pos - 1) % 10
        row = 9 - (pos - 1) // 10
        x = col * 60 + 30
        y = row * 60 + 30
        self.canvas.coords(self.players[player], x - 10, y - 10, x + 10, y + 10)

    def update_player_indicator(self, player, position):
        self.player_indicators[player].config(text=f"{self.players_names[player]}: {position}")


if __name__ == "__main__":
    root = tk.Tk()

    player1_name = simpledialog.askstring("Player 1 Name", "Enter Player 1's Name:")
    player2_name = simpledialog.askstring("Player 2 Name", "Enter Player 2's Name:")
    if player1_name and player2_name:
        app = SnakeNLadder(root)
        app.players_names = [player1_name, player2_name]
    else:
        app = SnakeNLadder(root)

    root.mainloop()
