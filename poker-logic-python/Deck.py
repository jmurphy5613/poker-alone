# from Card import Rank, Suit, Card
# import random

# class Deck:

#     deck = []

#     def __init__(self):
#         for rank in Rank:
#             for suit in Suit:
#                 self.deck.append(Card(rank, suit))

#     def __str__(self):
#         string = ''
#         for card in self.deck:
#             string = ''.join([string, f"{card.suit} {card.rank}\n"])
#         return string
    
#     def shuffle(self):
#         newDeck = []
#         while(len(self.deck) > 0):
#             randCard = random.choice(self.deck)
#             newDeck.append(randCard)
#             self.deck.remove(randCard)

#         self.deck = newDeck

#     def draw(self):
#         return self.deck.pop()

    