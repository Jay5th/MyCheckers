from DataSetup import GameData
from PlayerData import PlayerData

p1_data = PlayerData(1, 'Black')
p2_data = PlayerData(2, 'Red')
default_game = GameData(p1_data=p1_data, p2_data=p2_data, square_colors=('brown3', 'gray10'), window_width=750,
                        window_height=950)
