from board import GameBoard

class Game:
    def __init__(self, board, num_players):
        self.board = board
        self.num_players = num_players
        self.current_player = 0
        self.board.bind("<Button-1>", self.handle_dice_click)
        self.players_won = [False] * num_players

    def start(self):
        self.board.update_player_positions()
        self.board.display_turn(self.current_player)

    def handle_dice_click(self, event):
        if not self.board.is_game_over():
            if self.board.get_current_player() == self.current_player:
                dice_roll = self.board.roll_dice()
                self.board.display_dice_roll(dice_roll)
                self.move_player(dice_roll)

    def move_player(self, steps):
        current_player_index = self.board.get_current_player()
        self.board.move_player(current_player_index, steps)
        self.board.update_player_positions()

        current_position = self.board.player_positions[current_player_index]
        if current_position == 100:
            self.players_won[current_player_index] = True
            self.check_game_over()

        if not self.board.is_game_over():
            self.board.next_turn()
            self.current_player = (self.current_player + 1) % self.num_players
            self.board.display_turn(self.current_player)

    def check_game_over(self):
        if all(self.players_won):
            self.board.set_game_over()
            self.board.display_winner(self.current_player)

if __name__ == "__main__":
    board = GameBoard(None, 2)
    game = Game(board, 2)
    game.start()
    board.mainloop()
