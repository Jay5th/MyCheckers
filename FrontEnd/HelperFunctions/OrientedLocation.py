def oriented_location(x, y, center, orientation):
    oriented_x = x * orientation + (1 - orientation) * center[0]
    oriented_y = y * orientation + (1 - orientation) * center[1]
    return oriented_x, oriented_y
