from BackEnd.MoveLogic.Jump import jumps_at
from BackEnd.MoveLogic.Slide import slides_at


def legal_moves(board, player):
    move_dict = {}
    jumper_found = False
    sliders = []
    piece_addresses = [*player.king_locations, *player.man_locations]
    for address in piece_addresses:
        jumps = jumps_at(board, address)
        if len(jumps) > 0:
            jumper_found = True
            move_dict[address] = jumps
            continue
        if not jumper_found:
            slides = slides_at(board, address)
            if len(slides) == 0:
                continue
            move_dict[address] = slides
            sliders.append(address)
    if jumper_found:
        for address in sliders:
            move_dict.pop(address)
    return move_dict
