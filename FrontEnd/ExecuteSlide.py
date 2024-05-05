from BackEnd.Objects.CheckerPiece import CheckerPiece as LogicPiece
from FrontEnd.HelperFunctions.AddressToLocation import address_to_location
from FrontEnd.HelperFunctions.OrientedLocation import oriented_location


def execute_slide(current_player, current_board, drawn_pieces, start_address, end_address, orientation, center):
    logic_piece = current_board.get_entry(start_address)
    current_board.move_piece(start_address, end_address)
    piece = drawn_pieces[start_address]
    piece.place(*oriented_location(*address_to_location(end_address), center, orientation))
    drawn_pieces[end_address] = piece
    drawn_pieces.pop(start_address)
    if logic_piece.is_king:
        current_player.king_locations.remove(start_address)
        current_player.king_locations.append(end_address)
    else:
        current_player.man_locations.remove(start_address)
        if logic_piece.can_promote_at(end_address):
            current_board.replace_entry(end_address, LogicPiece(logic_piece.player_id, is_king=True))
            piece.promote()
            current_player.king_locations.append(end_address)
        else:
            current_player.man_locations.append(end_address)
