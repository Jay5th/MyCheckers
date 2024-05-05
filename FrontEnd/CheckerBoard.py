def draw_checker_board(canvas, side_length, center, colors):
    x, y = center
    top_left = (x - side_length // 2, y - side_length // 2)
    square_side_length = side_length // 8
    for i in range(8):
        for j in range(8):
            color = colors[(i + j) % 2]
            square_top_left = (top_left[0] + j * square_side_length,
                               top_left[1] + i * square_side_length)
            square_bottom_right = (top_left[0] + (j + 1) * square_side_length,
                                   top_left[1] + (i + 1) * square_side_length)
            canvas.create_rectangle(*square_top_left, *square_bottom_right, fill=color)
