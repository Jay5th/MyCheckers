from FrontEnd.HelperFunctions.AddressToLocation import address_to_location
from FrontEnd.HelperFunctions.LocationToAddress import location_to_address


def select_address(x, y, piece_radius):
    row, column = location_to_address(x, y)
    square_center_x, square_center_y = address_to_location((row, column))
    squared_distance_from_center = (x - square_center_x) ** 2 + (y - square_center_y) ** 2
    if squared_distance_from_center <= piece_radius ** 2:
        return row, column
    return None
