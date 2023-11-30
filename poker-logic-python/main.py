from Game import Game
from treys import Card, Evaluator

# game = Game(1000, ["jimmy", "john", "jack"])
# print(game.deck)
# game.deck.shuffle()
# print(game.deck)

evaluator = Evaluator()

board = [
    Card.new('Ah'),
    Card.new('Kd'),
    Card.new('Jc')
]

hand = [
   Card.new('Qs'),
   Card.new('Th')
]

Card.print_pretty_cards(board + hand)
print(evaluator.evaluate(board, hand))