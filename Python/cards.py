import random

suits = ['♠', '♥', '♦', '♣']  # Spades, Hearts, Diamonds, Clubs
ranks = ['A'] + [str(n) for n in range(2, 11)] + ['J', 'Q', 'K']
values = {'A': 11, 'J': 10, 'Q': 10, 'K': 10, **{str(n): n for n in range(2, 11)}}

class BJ_Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def value(self):
        return values[self.rank]

    def __str__(self):
        return f"{self.rank}{self.suit}"

    def image_filename(self):
        suit_names = {'♠': 'spades', '♥': 'hearts', '♦': 'diamonds', '♣': 'clubs'}
        rank_names = {'A': 'ace', 'J': 'jack', 'Q': 'queen', 'K': 'king', **{str(n): str(n) for n in range(2, 11)}}
        return f"images/{rank_names[self.rank]}_of_{suit_names[self.suit]}.png"

class BJ_Deck:
    def __init__(self):
        self.cards = [BJ_Card(s, r) for s in suits for r in ranks]
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()
