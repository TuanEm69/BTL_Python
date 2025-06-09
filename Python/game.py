from cards import BJ_Deck

class BJ_Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def value(self):
        total = sum(card.value() for card in self.cards)
        aces = sum(1 for card in self.cards if card.rank == 'A')
        while total > 21 and aces:
            total -= 10
            aces -= 1
        return total

    def is_blackjack(self):
        return len(self.cards) >= 2 and self.value() == 21

    def __str__(self):
        return ', '.join(str(card) for card in self.cards)

class BJ_Game:
    def __init__(self):
        self.deck = BJ_Deck()
        self.player = BJ_Hand()
        self.dealer = BJ_Hand()
        self.result = ""
        self.is_over = False
        self.start_game()

    def start_game(self):
        self.player = BJ_Hand()
        self.dealer = BJ_Hand()
        self.is_over = False
        self.result = ""
        self.player.add_card(self.deck.deal_card())
        self.player.add_card(self.deck.deal_card())
        self.dealer.add_card(self.deck.deal_card())
        self.dealer.add_card(self.deck.deal_card())

    def player_hit(self):
        self.player.add_card(self.deck.deal_card())
        if self.player.value() > 21:
            self.is_over = True
            self.result = "Cháy rồi Cu ơi! Thua!"

    def stand(self):
        while self.dealer.value() < 17:
            self.dealer.add_card(self.deck.deal_card())

        self.is_over = True
        self.result = self.check_winner()

    def check_winner(self):
        if self.player.is_blackjack():
            return "Blackjack! Bạn thắng!"
        if self.dealer.value() > 21:
            return "BOT cháy! Bạn thắng!"
        if self.player.value() > 21:
            return "Bạn cháy! Thua!"
        if self.player.value() > self.dealer.value():
            return "Bạn thắng!"
        elif self.player.value() < self.dealer.value():
            return "BOT thắng!"
        else:
            return "Hòa!"
