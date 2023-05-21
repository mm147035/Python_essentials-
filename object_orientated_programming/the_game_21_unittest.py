import unittest
from unittest.mock import patch
import io
import sys
import random

from the_game_21 import draw_card, play_game


class TestGame(unittest.TestCase):

    """test_draw_card(): This test case verifies the draw_card() function, which randomly selects a number between 1 and 10 (inclusive) and returns it.
    The test uses the side_effect parameter of the patch() decorator to specify a sequence of numbers to be returned by the random.randint() function, and then calls draw_card() four times to check that it returns the expected values. Finally, the test asserts that random.randint() was called with the expected arguments."""

    @patch('random.randint', side_effect=[1, 10, 4, 5])
    def test_draw_card(self, mock_randint):
        self.assertEqual(draw_card(), 1)
        self.assertEqual(draw_card(), 10)
        self.assertEqual(draw_card(), 4)
        self.assertEqual(draw_card(), 5)
        mock_randint.assert_called_with(1, 10)

    """ test_play_game_no_draw(): This test case verifies the play_game() function when the player chooses to "stand" (i.e., not draw any more cards). 
    The test uses the side_effect parameter of the patch() decorator to specify a sequence of numbers to be returned by the random.
    randint() function (corresponding to the dealer's card values), and simulates the player's input by using the side_effect parameter of another patch() decorator. 
    The test asserts that play_game() outputs the expected message and that random.randint() was called with the expected arguments.
    """

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.randint', side_effect=[10, 6, 2])
    @patch('builtins.input', side_effect=['n'])
    def test_play_game_no_draw(self, mock_input, mock_randint, mock_stdout):
        play_game()
        self.assertEqual(mock_stdout.getvalue().strip(), 'Your score is 16\nDealer\'s score is 2\nYou win!')
        mock_randint.assert_called_with(1, 10)

    """test_play_game_with_draw(): This test case verifies the play_game() function when the player chooses to "hit" (i.e., draw one more card). 
    The test uses a similar approach as the previous test case to simulate the player's input and the dealer's card values. 
    The test asserts that play_game() outputs the expected message and that random.randint() was called with the expected arguments.
    """

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.randint', side_effect=[10, 6, 6, 2])
    @patch('builtins.input', side_effect=['y', 'n'])
    def test_play_game_with_draw(self, mock_input, mock_randint, mock_stdout):
        play_game()
        self.assertEqual(mock_stdout.getvalue().strip(), 'Your score is 16\nDealer\'s score is 2\nYou win!')
        mock_randint.assert_called_with(1, 10)

    """test_play_game_player_bust(): This test case verifies the play_game() function when the player's card values exceed 21, resulting in a "bust". 
    The test uses a similar approach as the previous test cases to simulate the player's input and the dealer's card values. 
    The test asserts that play_game() outputs the expected message and that random.randint() was called with the expected arguments.
    """

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.randint', side_effect=[10, 5, 5, 6])
    @patch('builtins.input', side_effect=['y', 'n'])
    def test_play_game_player_bust(self, mock_input, mock_randint, mock_stdout):
        play_game()
        self.assertEqual(mock_stdout.getvalue().strip(), 'Your score is 15\nYou bust! Dealer wins.')
        mock_randint.assert_called_with(1, 10)

    """test_play_game_dealer_bust(): This test case verifies the play_game() function when the dealer's card values exceed 21, resulting in a "bust".
     The test uses a similar approach as the previous test cases to simulate the player's input and the dealer's card values.
      The test asserts that play_game() outputs the expected message and that random.randint() was called with the expected arguments.
    """

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.randint', side_effect=[10, 5, 6, 5])
    @patch('builtins.input', side_effect=['y', 'n'])
    def test_play_game_dealer_bust(self, mock_input, mock_randint, mock_stdout):
        play_game()
        self.assertEqual(mock_stdout.getvalue().strip(),
                         'Your score is 15\nDealer\'s score is 11\nDealer busts! You win.')
        mock_randint.assert_called_with(1, 10)

    """test_play_game_tie(): This test case verifies the play_game() function when both the player's and the dealer's card values are the same.
     The test uses a similar approach as the previous test cases to simulate the player's input and the dealer's card values.
      The test asserts that play_game() outputs the expected message and that random.randint() was called with the expected arguments.
    """

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.randint', side_effect=[10, 5, 6, 6])
    @patch('builtins.input', side_effect=['y', 'n'])
    def test_play_game_tie(self, mock_input, mock_randint, mock_stdout):
        play_game()
        self.assertEqual(mock_stdout.getvalue().strip(), 'Your score is 15\nDealer\'s score is 16\nIt\'s a tie.')
        mock_randint.assert_called_with(1, 10)


if __name__ == '__main__':
    unittest.main()


"""All of these test cases are designed to verify the correct behavior of the draw_card() and play_game() functions, given specific input values and card draws.
 They also ensure that the output messages are correct and that the random.randint() function is called with the expected arguments.
"""