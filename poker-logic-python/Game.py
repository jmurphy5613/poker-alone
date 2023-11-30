from treys import Deck
from Player import Player

class Game:

    players = []

    current_big_blind = 1
    current_small_blind = 2

    pot = 0

    def __init__(self, stack_size, bb, sb, names):
        for name in names:
            self.players.append(Player(stack_size, name))
        self.bb = bb
        self.sb = sb
        self.deck = Deck()

    def __str__(self):
        string = ''
        for player in self.players:
            string += f"{player.name}   {player.stack_size} \n"
        
        #display the pot amount
        string += f"\nPot: {self.pot} \n"
        string += f"{self.bb}/{self.sb}"
        return string
    
    def collectBets(self):
        big_blind = self.players[self.current_big_blind]
        small_blind = self.players[self.current_small_blind]
        self.pot += big_blind.bet(self.bb) + small_blind.bet(self.sb)

    def deal(self):
        #deal two cards to each player
        for player in self.players:
            player.hand.append(self.deck.draw(2))