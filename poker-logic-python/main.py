from Game import Game
from treys import Card, Evaluator
import os

game = Game(1000, 25, 50, ["jimmy", "john", "jack"])
game.deck.shuffle()
print(game.deck)
# print(game)
# os.system('clear')
# game.collectBets()
# game.deal()
# print(game)

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