from random import shuffle


class Card:

    def __init__(self, suit, value):
        self.suit = suit  # "Hearts", "Diamonds", "Clubs", or "Spades"
        self.value = value  # "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"

    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck:

    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = [
            "A",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "J",
            "Q",
            "K"]
        self.cards = [Card(suit, value) for suit in suits for value in values]

    def __repr__(self):
        return f"Deck of {self.count()} cards"

    def count(self):
        return len(self.cards)

    def _deal(self, num):
		count = self.count()
		actual = min([count,num])
		if count == 0:
			raise ValueError("All cards have been dealt")
		cards = self.cards[-actual:]
		self.cards = self.cards[:-actual]
		return cards
        
            

    def shuffle(self):
        if len(self.cards) < 52:
            raise ValueError("Only full decks can be shuffled")
        shuffle(self.cards)
        return self.cards

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, num_cards):
        return self._deal(num_cards)


deck = Deck()
print(deck)
deck.shuffle()
print(deck.deal_card())
print(deck)
print(deck.deal_hand(5))
print(deck)
