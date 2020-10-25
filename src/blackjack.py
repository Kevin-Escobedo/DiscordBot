import random
from card import Card

class Blackjack:
    def __init__(self):
        self.values = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        self.suits = ["Heart", "Diamond", "Club", "Spade"]
        self.deck = [Card(value, suit) for value in self.values for suit in self.suits]
        self.playerTotal = 0
        self.dealerTotal = 0
        self.playerHand = []
        self.dealerHand = []

    def hit(self, hand: [Card]) -> None:
        '''Adds a card to a hand'''
        random.shuffle(self.deck)
        card = self.deck.pop()
        self.hand.append(card)
