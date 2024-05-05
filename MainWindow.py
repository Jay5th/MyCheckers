import tkinter as tk
from GameSetup import default_game
from FrontEnd.GameBoard import GameBoard
from BackEnd.Objects.StartingBoard import create_starting_logic_board

current_game = default_game
game_board_size = (current_game.get_game_board_width(), current_game.get_game_board_height())
square_side_length = current_game.get_checker_board_side_length() // 8
square_colors = current_game.square_colors
p1_data = current_game.p1_data
p2_data = current_game.p2_data
player_id_to_color = {p1_data.id: p1_data.color, p2_data.id: p2_data.color}
logic_board = create_starting_logic_board(player_1_id=p1_data.id, player_2_id=p2_data.id)

root = tk.Tk()
root.configure(background='cadetblue2')
root.title('Checkers')
game_text = tk.Label(root, text='Player 1', font=('Arial', 26))
game_text.pack()

canvas = tk.Canvas(root, width=current_game.window_width, height=current_game.window_height, bg='chartreuse4')
game_board = GameBoard(canvas, current_game.get_window_center(), game_board_size, square_side_length, square_colors,
                       player_id_to_color, game_text, do_flip=False)

game_board.game_setup(logic_board, p1_data.id, p2_data.id)
game_board.bindings()

canvas.pack()

root.mainloop()
