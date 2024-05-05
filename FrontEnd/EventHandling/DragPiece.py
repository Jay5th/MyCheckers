def drag_piece(event, selected_piece):
    x = event.x
    y = event.y
    current_x, current_y = selected_piece.location()
    dx = x - current_x
    dy = y - current_y
    selected_piece.drag(dx, dy)
