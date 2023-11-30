from Deck import Deck
from Player import Player

class Game:
    def __init__(self, stack_size, names):
        self.players = {}
        for name in names:
            self.players.append(Player(stack_size, name))

        self.deck = Deck()

    