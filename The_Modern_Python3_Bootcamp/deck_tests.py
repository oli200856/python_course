from deck_of_cards import Card, Deck
from isiterator import is_iterator
import unittest


class CardTests(unittest.TestCase):

    def setUp(self):
        self.c = Card("Hearts", "A")

    def test_init(self):
        """__init__ should set the suit to be 'Hearts' and value to be 'A'"""
        self.assertEqual(self.c.suit, "Hearts")
        self.assertEqual(self.c.value, "A")

    def test_repr(self):
        """__repr__ function should return 'A of Hearts'"""
        self.assertEqual(repr(self.c), "A of Hearts")


class DeckTests(unittest.TestCase):

    def setUp(self):
        self.d = Deck()

    def test_init(self):
        """__init__ should set self.cards to be a list of 52 cards in deck"""
        self.assertTrue(isinstance(self.d.cards, list))
        self.assertEqual(len(self.d.cards), 52)

    def test_repr_full_deck(self):
        """__repr__ should return number of cards in deck (52)"""
        self.assertEqual(repr(self.d), "Deck of 52 cards")

    def test_repr_smaller_deck(self):
        """__repr__ should return number of cards in deck (51)"""
        self.d.cards.pop()
        self.assertEqual(repr(self.d), "Deck of 51 cards")
    
    def test_iter(self):
        """__iter__ should return iterable"""
        self.assertTrue(is_iterator(iter(self.d)))

    def test_count(self):
        """count should return number of cards in deck; 52 if full"""
        self.assertEqual(self.d.count(), 52)
        self.d.cards.pop()
        self.assertEqual(self.d.count(), 51)

    def test_deal_sufficient_cards(self):
        """_deal should deal provided number of cards"""
        cards = self.d._deal(10)
        self.assertEqual(len(cards), 10)
        self.assertEqual(self.d.count(), 42)

    def test_deal_insufficient_cards(self):
        """_deal should deal number of cards left in deck"""
        cards = self.d._deal(100)
        self.assertEqual(len(cards), 52)
        self.assertEqual(self.d.count(), 0)

    def test_deal_empty_deck(self):
        """when the deck is empty, _deal should raise ValueError"""
        self.d.cards = []
        with self.assertRaises(ValueError):
            self.d._deal(1)

    def test_deal_card(self):
        """deal_card should return a card from top of the deck and remove it from the deck"""
        card = self.d.cards[-1]
        dealt_card = self.d.deal_card()
        self.assertEqual(card, dealt_card)
        self.assertEqual(self.d.count(), 51)

    def test_deal_hand(self):
        """deal_hand should return specified number of cards from top of the deck and remove them"""
        cards = self.d.deal_hand(4)
        self.assertEqual(len(cards), 4)
        self.assertEqual(self.d.count(), 48)

    def test_shuffle_full_deck(self):
        """shuffle should change the order of the cards randomly"""
        cards = self.d.cards[:]
        self.d.shuffle()
        self.assertNotEqual(self.d.cards, cards_before)
        self.assertEqual(self.d.count(), 52)

    def test_shuffle_incomplete_deck(self):
        """if deck is incomplete, shuffle should raise ValueError"""
        self.d.cards.pop()
        with self.assertRaises(ValueError):
            self.d.shuffle()

if __name__ == "__main__":
    unittest.main()
