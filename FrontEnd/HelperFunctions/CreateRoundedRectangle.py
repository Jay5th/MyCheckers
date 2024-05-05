# Adapted from https://pythonhint.com/post/6368626835129927/how-to-make-a-tkinter-canvas-rectangle-with-rounded
# -corners#:~:text=To%20create%20a%20tkinter%20Canvas%20rectangle%20with%20rounded,
# root%20%3D%20Tk%28%29%20canvas%20%3D%20Canvas%28root%2C%20width%3D200%2C%20height%3D200%29


def create_rounded_rectangle(canvas, size, center, radius, fill_color):
    x1 = center[0] - size[0] // 2
    y1 = center[1] - size[1] // 2
    x2 = center[0] + size[0] // 2
    y2 = center[1] + size[1] // 2
    points = [x1 + radius, y1,
              x1 + radius, y1,
              x2 - radius, y1,
              x2 - radius, y1,
              x2, y1,
              x2, y1 + radius,
              x2, y1 + radius,
              x2, y2 - radius,
              x2, y2 - radius,
              x2, y2,
              x2 - radius, y2,
              x2 - radius, y2,
              x1 + radius, y2,
              x1 + radius, y2,
              x1, y2,
              x1, y2 - radius,
              x1, y2 - radius,
              x1, y1 + radius,
              x1, y1 + radius,
              x1, y1]

    canvas.create_polygon(*points, outline='black', fill=fill_color, width=2, smooth=True)
