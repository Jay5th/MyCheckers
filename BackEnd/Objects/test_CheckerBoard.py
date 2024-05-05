import unittest

from GameSetup import default_game
from CheckerBoard import CheckerBoard
from CheckerPiece import CheckerPiece


p1_man = CheckerPiece(default_game.p1_data.id)
p2_man = CheckerPiece(default_game.p2_data.id)
empty_matrix = [[None for j in range(8)] for i in range(8)]
empty_board = CheckerBoard(empty_matrix)
starting_matrix = list(empty_matrix)
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 1:
            if i in (0, 1, 2):
                starting_matrix[i][j] = p2_man
            elif i in (5, 6, 7):
                starting_matrix[i][j] = p1_man
starting_board = CheckerBoard(starting_matrix)


class TestCheckerBoard(unittest.TestCase):
    def test_get_entry(self):
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0:
                    continue
                # Test empty board
                self.assertEqual(None, empty_board.get_entry((i, j)))

                # Test starting board
                if i < 3:
                    self.assertEqual(p2_man, starting_board.get_entry((i, j)))
                elif i > 4:
                    self.assertEqual(p1_man, starting_board.get_entry((i, j)))
                else:
                    self.assertEqual(None, starting_board.get_entry((i, j)))

    def test_replace_entry(self):
        pass

    def test_move_piece(self):
        pass

if __name__ == '__main__':
    unittest.main()
