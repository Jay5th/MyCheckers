from dataclasses import dataclass
from PlayerData import PlayerData


@dataclass(frozen=True)
class GameData:
    p1_data: PlayerData
    p2_data: PlayerData
    square_colors: tuple[str, str]
    window_height: int
    window_width: int

    def get_player_color(self, player_id: int):
        if player_id == self.p1_data.id:
            return self.p1_data.color
        if player_id == self.p2_data.id:
            return self.p2_data.color
        raise ValueError(f"neither player has {player_id} as their id")

    def get_game_board_width(self):
        return int(self.window_width * 0.8)

    def get_game_board_height(self):
        return int(self.window_height * 0.8)

    def get_window_center(self):
        return self.window_width // 2, self.window_height // 2

    def get_checker_board_side_length(self):
        return int(0.8 * min(self.get_game_board_width(), self.get_game_board_height()))
