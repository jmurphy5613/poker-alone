from treys import Card, Deck, Evaluator

def evaluateStarting(hand):
    evaluator = Evaluator()
    totalStrength = 0
    simulatedFlops = 1000
    for i in range(simulatedFlops):
        deck = Deck()
        deck.shuffle()
        board = deck.draw(3)
        totalStrength += evaluator.evaluate(hand, board)
    averageStrength = totalStrength/simulatedFlops
    return evaluator.get_five_card_rank_percentage(averageStrength)

    