from FrontEnd.HelperFunctions.LocationToAddress import location_to_address


def drop_address(x, y, current_legal_moves, start_address):
    if start_address in current_legal_moves.keys():
        end_address = location_to_address(x, y)
        if end_address in current_legal_moves[start_address]:
            return end_address
    return start_address
