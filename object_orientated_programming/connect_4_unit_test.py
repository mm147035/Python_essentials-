import unittest
from connect_4 import ConnectFour

class TestConnectFour(unittest.TestCase):

    def setUp(self):
        self.game = ConnectFour()

    def test_drop_piece(self):
        self.assertIsNone(self.game.drop_piece(7)) # Invalid column
        self.assertEqual(self.game.drop_piece(0), (5, 0)) # Valid column

    def test_is_valid_location(self):
        self.assertFalse(self.game.is_valid_location(7)) # Invalid column
        self.assertTrue(self.game.is_valid_location(0)) # Valid column

    def test_get_next_open_row(self):
        self.assertEqual(self.game.get_next_open_row(0), 5) # Column with no pieces
        self.game.drop_piece(0)
        self.assertEqual(self.game.get_next_open_row(0), 4) # Column with one piece

    def test_winning_move(self):
        self.assertFalse(self.game.winning_move()) # No winning move
        self.game.board[5,0:4] = 1 # Horizontal winning move for player 1
        self.assertTrue(self.game.winning_move())

    def test_switch_turn(self):
        self.assertEqual(self.game.turn, 1)
        self.game.switch_turn()
        self.assertEqual(self.game.turn, 2)

    def test_is_game_over(self):
        self.assertFalse(self.game.is_game_over()) # Game is not over
        self.game.board[:,:] = 1 # Board is full
        self.assertTrue(self.game.is_game_over())

    def test_get_board(self):
        self.assertEqual(self.game.get_board().shape, (6, 7))

    def test_get_turn(self):
        self.assertEqual(self.game.get_turn(), 1)

if __name__ == '__main__':
    unittest.main()
