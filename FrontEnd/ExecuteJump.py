from FrontEnd.ExecuteSlide import execute_slide


def execute_jump(current_player, opponent, current_board, drawn_pieces, start_address, end_address, orientation, center):
    execute_slide(current_player, current_board, drawn_pieces, start_address, end_address, orientation, center)
    jumped_address = ((start_address[0] + end_address[0]) // 2, (start_address[1] + end_address[1]) // 2)
    jumped_logic_piece = current_board.get_entry(jumped_address)
    if jumped_logic_piece.is_king:
        opponent.king_locations.remove(jumped_address)
    else:
        opponent.man_locations.remove(jumped_address)
    current_board.replace_entry(jumped_address, None)
    jumped_piece = drawn_pieces[jumped_address]
    drawn_pieces.pop(jumped_address)
    return jumped_piece
