from unittest import TestCase, main
from unittest.mock import patch
from test_helper import run_test

class TestBlackjack(TestCase):

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_example(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand less than 21.
        The dealer wins by having a higher hand than the user.

        '''
        output = run_test([3, 5, 8], ['y', 'n'], [3, 5, 10], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "You have 8. Hit (y/n)? y\n" \
                   "Drew an 8\n" \
                   "You have 16. Hit (y/n)? n\n" \
                   "Final hand: 16.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "Dealer has 8.\n" \
                   "Drew a 10\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')

    def test_user_wins_greater_than_dealer(self, input_mock, randint_mock):

        output = run_test([1, 3, 6], ['y', 'n'], [8, 5, 4], randint_mock, input_mock)
        expected = "-----------\n" \
                    "YOUR TURN\n" \
                    "-----------\n" \
                    "Drew an Ace\n" \
                    "Drew a 3\n" \
                    "You have 14. Hit (y/n)? y\n" \
                    "Drew a 6\n" \
                    "You have 20. Hit (y/n)? n\n" \
                    "Final hand: 20.\n" \
                    "-----------\n" \
                    "DEALER TURN\n" \
                    "-----------\n" \
                    "Drew an 8\n" \
                    "Drew a 5\n" \
                    "Dealer has 13.\n" \
                    "Drew a 4\n" \
                    "Final hand: 17.\n" \
                    "-----------\n" \
                    "GAME RESULT\n" \
                    "-----------\n" \
                    "You win!\n"
        self.assertEqual(output, expected)    

    
    @patch('blackjack_helper.randint')
    @patch('builtins.input')    
    def test_user_wins_blackjack(self,input_mock, randint_mock):

        output = run_test([4, 8, 9], ['y', 'y', 'n'], [3, 9, 5], randint_mock, input_mock)
        expected = "-----------\n" \
                    "YOUR TURN\n" \
                    "-----------\n" \
                    "Drew a 4\n" \
                    "Drew an 8\n" \
                    "You have 12. Hit (y/n)? y\n" \
                    "Drew a 9\n" \
                    "Final hand: 21.\n" \
                    "BLACKJACK!\n" \
                    "-----------\n" \
                    "DEALER TURN\n" \
                    "-----------\n" \
                    "Drew a 3\n" \
                    "Drew a 9\n" \
                    "Dealer has 12.\n" \
                    "Drew a 5\n" \
                    "Final hand: 17.\n" \
                    "-----------\n" \
                    "GAME RESULT\n" \
                    "-----------\n" \
                    "You win!\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')    
    def test_user_wins_dealer_bust(self,input_mock, randint_mock):

        output = run_test([5,10,5], ['y','x','n'], [7, 8, 11], randint_mock, input_mock)
        expected = "-----------\n" \
                    "YOUR TURN\n" \
                    "-----------\n" \
                    "Drew a 5\n" \
                    "Drew a 10\n" \
                    "You have 15. Hit (y/n)? y\n" \
                    "Drew a 5\n" \
                    "You have 20. Hit (y/n)? x\n" \
                    "Sorry I didn't get that.\n" \
                    "You have 20. Hit (y/n)? n\n" \
                    "Final hand: 20.\n" \
                    "-----------\n" \
                    "DEALER TURN\n" \
                    "-----------\n" \
                    "Drew a 7\n" \
                    "Drew an 8\n" \
                    "Dealer has 15.\n" \
                    "Drew a Jack\n" \
                    "Final hand: 25.\n" \
                    "BUST.\n"\
                    "-----------\n" \
                    "GAME RESULT\n" \
                    "-----------\n" \
                    "You win!\n"
        self.assertEqual(output, expected) 

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_blackjack_dealer_bust(self,input_mock, randint_mock):

        output = run_test([5,9,7], ['y'], [12, 6, 13], randint_mock, input_mock)
        expected = "-----------\n" \
                    "YOUR TURN\n" \
                    "-----------\n" \
                    "Drew a 5\n" \
                    "Drew a 9\n" \
                    "You have 14. Hit (y/n)? y\n" \
                    "Drew a 7\n" \
                    "Final hand: 21.\n" \
                    "BLACKJACK!\n" \
                    "-----------\n" \
                    "DEALER TURN\n" \
                    "-----------\n" \
                    "Drew a Queen\n" \
                    "Drew a 6\n" \
                    "Dealer has 16.\n" \
                    "Drew a King\n" \
                    "Final hand: 26.\n" \
                    "BUST.\n"\
                    "-----------\n" \
                    "GAME RESULT\n" \
                    "-----------\n" \
                    "You win!\n"
        self.assertEqual(output, expected) 

    @patch('blackjack_helper.randint')
    @patch('builtins.input')    
    def test_dealer_wins_greater_than_user(self,input_mock, randint_mock):

        output = run_test([2, 10, 5], ['y','n'], [8, 6, 4], randint_mock, input_mock)
        expected = "-----------\n" \
                    "YOUR TURN\n" \
                    "-----------\n" \
                    "Drew a 2\n" \
                    "Drew a 10\n" \
                    "You have 12. Hit (y/n)? y\n" \
                    "Drew a 5\n" \
                    "You have 17. Hit (y/n)? n\n"\
                    "Final hand: 17.\n" \
                    "-----------\n" \
                    "DEALER TURN\n" \
                    "-----------\n" \
                    "Drew an 8\n" \
                    "Drew a 6\n" \
                    "Dealer has 14.\n" \
                    "Drew a 4\n" \
                    "Final hand: 18.\n" \
                    "-----------\n" \
                    "GAME RESULT\n" \
                    "-----------\n" \
                    "Dealer wins!\n"
        self.assertEqual(output, expected) 

    @patch('blackjack_helper.randint')
    @patch('builtins.input')    
    def test_dealer_wins_blackjack(self,input_mock, randint_mock):

        output = run_test([1, 9], ['n'], [7, 9, 5], randint_mock, input_mock)
        expected = "-----------\n" \
                    "YOUR TURN\n" \
                    "-----------\n" \
                    "Drew an Ace\n" \
                    "Drew a 9\n" \
                    "You have 20. Hit (y/n)? n\n" \
                    "Final hand: 20.\n" \
                    "-----------\n" \
                    "DEALER TURN\n" \
                    "-----------\n" \
                    "Drew a 7\n" \
                    "Drew a 9\n" \
                    "Dealer has 16.\n" \
                    "Drew a 5\n" \
                    "Final hand: 21.\n" \
                    "BLACKJACK!\n"\
                    "-----------\n" \
                    "GAME RESULT\n" \
                    "-----------\n" \
                    "Dealer wins!\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')    
    def test_dealer_wins_user_busts(self,input_mock, randint_mock):

        output = run_test([11,5,2,2,1], ['y','y','x','y'], [8, 8, 4], randint_mock, input_mock)
        expected = "-----------\n" \
                    "YOUR TURN\n" \
                    "-----------\n" \
                    "Drew a Jack\n" \
                    "Drew a 5\n" \
                    "You have 15. Hit (y/n)? y\n" \
                    "Drew a 2\n" \
                    "You have 17. Hit (y/n)? y\n" \
                    "Drew a 2\n" \
                    "You have 19. Hit (y/n)? x\n" \
                    "Sorry I didn't get that.\n" \
                    "You have 19. Hit (y/n)? y\n" \
                    "Drew an Ace\n" \
                    "Final hand: 30.\n" \
                    "BUST.\n"\
                    "-----------\n" \
                    "DEALER TURN\n" \
                    "-----------\n" \
                    "Drew an 8\n" \
                    "Drew an 8\n" \
                    "Dealer has 16.\n" \
                    "Drew a 4\n" \
                    "Final hand: 20.\n" \
                    "-----------\n" \
                    "GAME RESULT\n" \
                    "-----------\n" \
                    "Dealer wins!\n"
        self.assertEqual(output, expected) 

    @patch('blackjack_helper.randint')
    @patch('builtins.input')    
    def test_dealer_wins_both_bust(self,input_mock, randint_mock):

        output = run_test([1,1], [], [8, 8, 13], randint_mock, input_mock)
        expected = "-----------\n" \
                    "YOUR TURN\n" \
                    "-----------\n" \
                    "Drew an Ace\n" \
                    "Drew an Ace\n" \
                    "Final hand: 22.\n" \
                    "BUST.\n"\
                    "-----------\n" \
                    "DEALER TURN\n" \
                    "-----------\n" \
                    "Drew an 8\n" \
                    "Drew an 8\n" \
                    "Dealer has 16.\n" \
                    "Drew a King\n" \
                    "Final hand: 26.\n" \
                    "BUST.\n"\
                    "-----------\n" \
                    "GAME RESULT\n" \
                    "-----------\n" \
                    "Dealer wins!\n"
        self.assertEqual(output, expected) 

    @patch('blackjack_helper.randint')
    @patch('builtins.input')    
    def test_push_both_tie(self,input_mock, randint_mock):

        output = run_test([7,6,5], ['x','y','n'], [1, 5, 2], randint_mock, input_mock)
        expected = "-----------\n" \
                    "YOUR TURN\n" \
                    "-----------\n" \
                    "Drew a 7\n" \
                    "Drew a 6\n" \
                    "You have 13. Hit (y/n)? x\n" \
                    "Sorry I didn't get that.\n" \
                    "You have 13. Hit (y/n)? y\n" \
                    "Drew a 5\n" \
                    "You have 18. Hit (y/n)? n\n" \
                    "Final hand: 18.\n" \
                    "-----------\n" \
                    "DEALER TURN\n" \
                    "-----------\n" \
                    "Drew an Ace\n" \
                    "Drew a 5\n" \
                    "Dealer has 16.\n" \
                    "Drew a 2\n" \
                    "Final hand: 18.\n" \
                    "-----------\n" \
                    "GAME RESULT\n" \
                    "-----------\n" \
                    "Push.\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')    
    def test_push_both_blackjack(self,input_mock, randint_mock):

        output = run_test([3,2,5,2,7,2], ['y','y','y','y'], [1, 4, 6], randint_mock, input_mock)
        expected = "-----------\n" \
                    "YOUR TURN\n" \
                    "-----------\n" \
                    "Drew a 3\n" \
                    "Drew a 2\n" \
                    "You have 5. Hit (y/n)? y\n" \
                    "Drew a 5\n" \
                    "You have 10. Hit (y/n)? y\n" \
                    "Drew a 2\n" \
                    "You have 12. Hit (y/n)? y\n" \
                    "Drew a 7\n" \
                    "You have 19. Hit (y/n)? y\n" \
                    "Drew a 2\n" \
                    "Final hand: 21.\n" \
                    "BLACKJACK!\n" \
                    "-----------\n" \
                    "DEALER TURN\n" \
                    "-----------\n" \
                    "Drew an Ace\n" \
                    "Drew a 4\n" \
                    "Dealer has 15.\n" \
                    "Drew a 6\n" \
                    "Final hand: 21.\n" \
                    "BLACKJACK!\n"\
                    "-----------\n" \
                    "GAME RESULT\n" \
                    "-----------\n" \
                    "Push.\n"
        self.assertEqual(output, expected)

if __name__ == '__main__':
    main()