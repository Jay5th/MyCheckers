import unittest
from LegalMoves import legal_moves
from GameSetup import default_game
from BackEnd.Objects.CheckerBoard import CheckerBoard
from BackEnd.Objects.CheckerPiece import CheckerPiece
from BackEnd.Objects.Player import Player

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
test_matrix[3][2] = p2_man
test_board = CheckerBoard(test_matrix)


class LegalMovesTest(unittest.TestCase):
    def test_legal_moves(self):
        # starting board player 1
        player_1 = Player(default_game.p1_data.id, starting_board)
        true_legal_moves = {(5, 0): [(4, 1)],
                            (5, 2): [(4, 1), (4, 3)],
                            (5, 4): [(4, 3), (4, 5)],
                            (5, 6): [(4, 5), (4, 7)]}
        test_legal_moves = legal_moves(starting_board, player_1)
        for address in true_legal_moves.keys():
            true_moves = sorted(true_legal_moves[address])
            test_moves = sorted(test_legal_moves[address])
            self.assertEqual(true_moves, test_moves), "failed starting board test for player 1"

        # test board player 1
        player_1 = Player(default_game.p1_data.id, test_board)
        true_legal_moves = {(2, 3): [(4, 1), (4, 5)]}
        test_legal_moves = legal_moves(test_board, player_1)
        for address in true_legal_moves.keys():
            true_moves = sorted(true_legal_moves[address])
            test_moves = sorted(test_legal_moves[address])
            self.assertEqual(true_moves, test_moves), "failed test board test for player 1"



if __name__ == '__main__':
    unittest.main()
