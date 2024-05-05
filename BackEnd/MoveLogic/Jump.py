from BackEnd.MoveLogic.MoveHelperFunction import addresses_reachable_by_slide_xor_jump


def jumps_at(board, address):
    piece = board.get_entry(address)
    if piece is None:
        return []
    reachable_addresses = addresses_reachable_by_slide_xor_jump(board, address, "jump")
    end_addresses = []
    for end_address in reachable_addresses:
        if not (board.get_entry(end_address) is None):
            continue
        middle_address = ((address[0] + end_address[0]) // 2, (address[1] + end_address[1]) // 2)
        middle_entry = board.get_entry(middle_address)
        if middle_entry is None:
            continue
        if piece.player_id != middle_entry.player_id:
            end_addresses.append(end_address)
    return end_addresses
