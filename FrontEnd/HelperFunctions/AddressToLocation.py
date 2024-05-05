from GameSetup import default_game
game_board_center = default_game.get_window_center()
square_side_length = default_game.get_checker_board_side_length() // 8


def address_to_location(address):
    top_left = (game_board_center[0] - 4 * square_side_length, game_board_center[1] - 4 * square_side_length)
    row, column = address
    x = int((column + 1 / 2) * square_side_length) + top_left[0]
    y = int((row + 1 / 2) * square_side_length) + top_left[1]
    return x, y
