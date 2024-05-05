from BackEnd.MoveLogic.MoveHelperFunction import addresses_reachable_by_slide_xor_jump


def slides_at(board, address):
    piece = board.get_entry(address)
    if piece is None:
        return []
    reachable_addresses = addresses_reachable_by_slide_xor_jump(board, address, "slide")
    return [end_address for end_address in reachable_addresses if board.get_entry(end_address) is None]
