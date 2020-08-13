import unittest

from src.card import Card
from src.card_game import CardGame

class CardGameTest(unittest.TestCase):

    def setUp(self):
        self.game = CardGame()
    
    def test_ace_function__true(self):
        card = Card('spades', 1)
        self.assertEqual(True, self.game.checkforAce(card))

    def test_ace_function__false(self):
        card = Card('spades', 2)
        self.assertEqual(False, self.game.checkforAce(card))

    def test_highest_card__1(self):
        card1 = Card('spades', 3)
        card2 = Card('spades', 1)
        self.assertEqual(card1, self.game.highest_card(card1, card2))

    def test_highest_card__2(self):
        card1 = Card('spades', 1)
        card2 = Card('spades', 3)
        self.assertEqual(card2, self.game.highest_card(card1, card2))

    def test_card_count(self):
        card1 = Card('spades', '1')
        card2 = Card('spades', '3')
        cards = [card1, card2]
        self.assertEqual('You have a total of13', self.game.cards_total(cards))