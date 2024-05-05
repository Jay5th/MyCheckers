from GameSetup import default_game


def addresses_reachable_by_slide_xor_jump(board, address, move):
    if move == "slide":
        distance = 1
    elif move == "jump":
        distance = 2
    else:
        raise ValueError("move must be a slide or jump")
    piece = board.get_entry(address)
    row, column = address
    row_changes_to_consider = {i for i in (-distance, distance) if (row + i) in range(8)}
    if not piece.is_king:
        if piece.player_id == default_game.p1_data.id:
            row_changes_to_consider -= {distance}
        else:
            row_changes_to_consider -= {-distance}
    column_changes_to_consider = {j for j in (-distance, distance) if (column + j) in range(8)}
    return [(row + i, column + j) for i in row_changes_to_consider for j in column_changes_to_consider]
