from GameSetup import default_game
game_board_center = default_game.get_window_center()
square_side_length = default_game.get_checker_board_side_length() // 8


def location_to_address(x, y):
    top_left = (game_board_center[0] - 4 * square_side_length, game_board_center[1] - 4 * square_side_length)
    column = int((x - top_left[0]) / square_side_length)
    row = int((y - top_left[1]) / square_side_length)
    if not ((0 <= row <= 7) and (0 <= column <= 7)):
        return -1, -1
    return row, column
