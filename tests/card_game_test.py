import unittest

from src.card import Card
from src.card_game import CardGame

class CardGameTest(unittest.TestCase):

    def setUp(self):
        self.game = CardGame()
    
    def test_ace_function__true(self):
        card = Card('spades', 1)
        self.assertAlmostEquals(True, self.game.checkforAce(card))