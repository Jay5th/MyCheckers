from Assets.CreatePieceImage import create_piece_image


class CheckerPiece:
    def __init__(self, canvas, radius, name):
        self.name = name
        self.radius = radius
        self.canvas = canvas
        self.image = create_piece_image(name, radius)
        self.piece_id = self.canvas.create_image(0, 0, image=self.image)

    def location(self):
        '''
        x0, y0, x1, y1 = self.canvas.coords(self.piece_id)
        center_x = (x0 + x1) // 2
        center_y = (y0 + y1) // 2
        '''
        return self.canvas.coords(self.piece_id)

    def place(self, x, y):
        center_x, center_y = self.location()
        displacement_x = x - center_x
        displacement_y = y - center_y
        self.canvas.move(self.piece_id, displacement_x, displacement_y)
        self.canvas.tag_raise(self.piece_id)

    def drag(self, dx, dy):
        self.canvas.move(self.piece_id, dx, dy)
        self.canvas.tag_raise(self.piece_id)

    def promote(self):
        self.name = self.name[0:-3] + "King"
        self.image = create_piece_image(self.name, self.radius)
        self.canvas.itemconfigure(self.piece_id, image=self.image)

    def delete(self):
        self.canvas.delete(self.piece_id)
        del self
