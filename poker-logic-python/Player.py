

class Player:
    def __init__(self, stack_size, name):
        self.stack_size = stack_size
        self.name = name
        self.hand = []

    def bet(self, amount):
        self.stack_size -= amount
        return amount