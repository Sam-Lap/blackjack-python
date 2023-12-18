'''
Portfolio Project
BLACKJACK
'''

class Card:
    def __init__(self, suit, value):
        # Initialize a new playing card.
        self.suit = suit
        self.value = value

    def __repr__(self):
        # Represent the card as a string for debugging.
        return f"Card('{self.suit}', '{self.value}')"

    def __str__(self):
        # Return a string representation of the card, e.g., "Ace of Spades".
        return f"{self.value} of {self.suit}"

    def get_value(self):
        # Get the numeric value of the card for Blackjack.
        # Returns: The numeric value of the card. For number cards, it's their number
        if self.value in ['Jack', 'Queen', 'King']:
            return 10
        elif self.value == 'Ace':
            return 11
        else:
            return int(self.value)
