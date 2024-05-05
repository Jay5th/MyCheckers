from GameSetup import default_game


class CheckerPiece:
    def __init__(self, player_id, is_king=False):
        self.player_id = player_id
        self.is_king = is_king

    def __str__(self):
        color = default_game.get_player_color(self.player_id)
        if self.is_king:
            return f"{color[0]}K"
        return f"{color[0]}M"

    def can_promote_at(self, address):
        if self.is_king:
            return False
        row, column = address
        if self.player_id == default_game.p1_data.id:
            if row == 0:
                return True
            return False
        if row == 7:
            return True
        return False
