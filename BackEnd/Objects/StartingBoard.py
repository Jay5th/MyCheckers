from BackEnd.Objects.CheckerBoard import CheckerBoard
from BackEnd.Objects.CheckerPiece import CheckerPiece


def create_starting_logic_board(player_1_id=0, player_2_id=1):
    p1_man = CheckerPiece(player_1_id)
    p2_man = CheckerPiece(player_2_id)
    starting_matrix = [[None for j in range(8)] for i in range(8)]
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 1:
                if i in (0, 1, 2):
                    starting_matrix[i][j] = p2_man
                elif i in (5, 6, 7):
                    starting_matrix[i][j] = p1_man
    return CheckerBoard(starting_matrix)
