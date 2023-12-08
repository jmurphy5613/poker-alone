from treys import Deck, Card, Evaluator
from Player import Player
import random

class Game:

    players = []
    current_big_blind = 1
    current_small_blind = 2
    current_turn = 0
    current_bet = 0
    board = []
    pot = 0
    is_preflop = True

    evaluator = Evaluator()

    def __init__(self, stack_size, bb, sb, names):
        for name in names:
            self.players.append(Player(stack_size, name))
        self.bb = bb
        self.sb = sb
        self.deck = Deck()

    def __str__(self):
        string = ''
        for player in self.players:
            string += f"{player.name} {player.stack_size}"
            if(self.players.index(player) == self.current_big_blind):
                string += " BB"
            elif(self.players.index(player) == self.current_small_blind):
                string += " SB"
            string += "\n"
            string += f"{Card.int_to_pretty_str(player.hand[0])} {Card.int_to_pretty_str(player.hand[1])} \n\n"

        if(len(self.board) > 0):
            string += "Board: "
            for card in self.board:
                string += f"{Card.int_to_pretty_str(card)} "
            string += "\n\n"
            
        #display the pot amount
        string += f"\nPot: {self.pot} \n"
        string += f"{self.bb}/{self.sb}"
        # add whitespace
        string += "\n\n\n\n\n\n\n"
        return string
    
    def collectBets(self):
        big_blind = self.players[self.current_big_blind]
        small_blind = self.players[self.current_small_blind]
        self.pot += big_blind.bet(self.bb) + small_blind.bet(self.sb)

    def deal(self):
        #deal two cards to each player
        for player in self.players:
            player.hand = self.deck.draw(2)

    def flop(self):
        self.board = self.deck.draw(3)

    def turn(self):
        self.board.append(self.deck.draw())
    
    def moveBlinds(self):
        self.current_big_blind = (self.current_big_blind - 1) % len(self.players)
        self.current_small_blind = (self.current_small_blind - 1) % len(self.players)

    def startingPosition(self):
        if(self.is_preflop):
            return (self.current_big_blind - 1) % len(self.players)
        else:
            # starting from the small blind, go around the table until you find the first player who hasn't folded
            current_position = self.current_small_blind
            while(self.players[current_position].hand == []):
                current_position = (current_position - 1) % len(self.players)
            return current_position


    def moveCurrentPosition(self):
        self.current_turn = (self.current_turn + 1) % len(self.players)

    def playerDoSomething(self):
        # options: fold, call, raise, check, 
        
        # Preflop Strategy:
        # if the hand is in the bottom 70% of hands preflop, fold
        # if the hand is in the top 20% of hands preflop, 3 bet
        # otherwise, call

        # Postflop Strategy:

        # betting range
        # if the current bet is 0 and the player has a hand in the top 20% of hands, 3bet

        # calling range
        # if the current bet is 0 and the player has a hand in the top 30% of hands, call

        # checking range
        

        current_player = self.players[self.current_turn]
        hand_rank = self.evaluator.evaluate(self.board, current_player.hand)
        hand_rank_percentage = self.evaluator.get_five_card_rank_percentage(hand_rank)
        if(self.is_preflop):
            if(hand_rank_percentage < 0.7):
                current_player.fold()
                return
            elif(hand_rank_percentage > 0.8):
                current_player.bet(self.current_bet * 3)
                return
            else:
                current_player.bet(self.current_bet)
                return
        else:
            



    