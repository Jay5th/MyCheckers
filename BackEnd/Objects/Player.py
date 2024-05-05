class Player:
    def __init__(self, player_id, board):
        self.player_id = player_id
        self.man_locations = []
        self.king_locations = []
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0:
                    continue
                address = (i, j)
                piece = board.get_entry(address)
                if piece is None:
                    continue
                if piece.player_id == self.player_id:
                    if piece.is_king:
                        self.king_locations.append(address)
                    else:
                        self.man_locations.append(address)
