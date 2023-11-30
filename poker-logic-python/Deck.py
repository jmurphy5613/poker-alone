from Card import Rank, Suit, Card

class Deck:
    def __init__(self):

        self.deck = []

        for rank in Rank:
            for suit in Suit:
                self.deck.append(Card(rank, suit))
    