from Game import Game
from treys import Card, Deck, Evaluator
import os

game = Game(1000, 50, 25, ["jimmy", "john", "jack", "jill", "natalie"])
game.deck.shuffle()
game.collectBets()
game.deal()
game.moveBlinds()
game.moveBlinds()
print(game)
game.moveBlinds()
print(game)
print(game.players[game.startingPosition(isPreflop=True)])
game.flop()
print(game)
print(game.players[game.startingPosition(isPreflop=False)])



# deck = Deck()
# hand = []
# hand.append(deck.draw(2))
# Card.print_pretty_cards(hand) 

# evaluator = Evaluator()

# board = [
#     Card.new('Ah'),
#     Card.new('Kd'),
#     Card.new('Jc')
# ]

# hand = [
#    Card.new('Qs'),
#    Card.new('Th')
# ]

# Card.print_pretty_cards(board + hand)
# print(evaluator.evaluate(board, hand))