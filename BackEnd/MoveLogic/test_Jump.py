import unittest

from GameSetup import default_game
from Jump import jumps_at
from BackEnd.Objects.CheckerBoard import CheckerBoard
from BackEnd.Objects.CheckerPiece import CheckerPiece

p1_man = CheckerPiece(default_game.p1_data.id)
p1_king = CheckerPiece(default_game.p1_data.id, is_king=True)
p2_man = CheckerPiece(default_game.p2_data.id)
p2_king = CheckerPiece(default_game.p2_data.id, is_king=True)
empty_matrix = [[None for j in range(8)] for i in range(8)]
empty_board = CheckerBoard(empty_matrix)
starting_matrix = [[None for j in range(8)] for i in range(8)]
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 1:
            if i in (0, 1, 2):
                starting_matrix[i][j] = p2_man
            elif i in (5, 6, 7):
                starting_matrix[i][j] = p1_man
starting_board = CheckerBoard(starting_matrix)
test_matrix = [[None for j in range(8)] for i in range(8)]
test_matrix[2][3] = p1_king
test_matrix[3][4] = p2_man
test_board = CheckerBoard(test_matrix)


class TestJump(unittest.TestCase):
    def test_jump(self):
        # Test no jumps
        address = (1, 4)
        self.assertEqual([], jumps_at(empty_board, address))

        # Test single jump
        address = (2, 3)
        self.assertEqual([(4, 5)], jumps_at(test_board, address))


if __name__ == '__main__':
    unittest.main()
