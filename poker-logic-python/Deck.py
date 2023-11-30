from Card import Rank, Suit, Card
from random import random

class Deck:
    def __init__(self):

        self.deck = []

        for rank in Rank:
            for suit in Suit:
                self.deck.append(Card(rank, suit))

    def __str__(self):
        string = ''
        for card in self.deck:
            string = ''.join([string, f"{card.suit} {card.rank}\n"])
        return string
    
    def shuffle(self):
        newDeck = []
        while(len(self.deck.length) > 0):
            randCard = random.choice(self.deck)
            newDeck.append(randCard)
        self.deck = newDeck

    