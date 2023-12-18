'''
Portfolio Project
BLACKJACK
'''
import random

class Card:
    def __init__(self, suit, value):
        # Initialize a new playing card
        self.suit = suit
        self.value = value

    def __repr__(self):
        # Represent the card as a string for debugging
        return f"Card('{self.suit}', '{self.value}')"

    def __str__(self):
        # Return a string representation of the card, e.g., "Ace of Spades"
        return f"{self.value} of {self.suit}"

    def get_value(self):
        # Get the numeric value of the card for Blackjack
        # Returns: The numeric value of the card. For number cards, it's their number
        if self.value in ['Jack', 'Queen', 'King']:
            return 10
        elif self.value == 'Ace':
            return 11
        else:
            return int(self.value)

class Deck:
    def __init__(self):
        # Initialize a new deck of 52 cards
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        self.cards = [Card(suit, value) for suit in suits for value in values]

    def shuffle(self):
        # Shuffle the deck of cards
        random.shuffle(self.cards)

    def deal_card(self):
        # Deal (remove and return) a card from the deck
        # If the deck is empty, a new deck is created and shuffled
        # Returns: The dealt card
        if len(self.cards) == 0:
            self.__init__()
            self.shuffle()
        return self.cards.pop()

    def __str__(self):
        # Return a string representation of the deck
        return ', '.join(str(card) for card in self.cards)

    def __len__(self):
        # Return the number of cards left in the deck
        return len(self.cards)

class Hand:
    def __init__(self):
        # Initialize a new hand for a player or dealer
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        # Add a card to the hand and adjust the hand's value
        self.cards.append(card)
        self.value += card.get_value()

        # Track Aces
        if card.value == 'Ace':
            self.aces += 1

        # Adjust for Aces if the total value exceeds 21
        self.adjust_for_ace()

    def adjust_for_ace(self):
        # Adjust the value of the hand if it contains an Ace and the value exceeds 21
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

    def is_bust(self):
        # Check if the hand's value exceeds 21 (bust)
        # Returns: True if hand value is over 21, False otherwise
        return self.value > 21

    def __str__(self):
        # Return a string representation of the hand
        return ', '.join(str(card) for card in self.cards) + f" (Value: {self.value})"


class Player:
    def __init__(self, name, chips=1000):
        # Initialize a new player
        self.name = name
        self.chips = chips
        self.hand = Hand()
        self.bet = 0

    def place_bet(self, amount):
        # Place a bet for the current round.
        # Returns: True if the bet is successfully placed, False if not enough chips
        if amount > self.chips:
            print("Not enough chips to place that bet.")
            return False
        else:
            self.bet = amount
            self.chips -= amount
            return True

    def win_bet(self):
        # Handle the player winning a bet
        self.chips += 2 * self.bet

    def push(self):
        # Handle a push (tie) situation where the player gets their bet back
        self.chips += self.bet

    def hit(self, deck):
        # Take a new card from the deck and add it to the player's hand
        self.hand.add_card(deck.deal_card())

    def is_bust(self):
        # Check if the player's hand is a bust
        # Returns: True if the player's hand value exceeds 21, False otherwise
        return self.hand.is_bust()

    def display_hand(self):
        # Display the player's hand and the current value
        print(f"{self.name}'s Hand: {self.hand}")

    def reset_hand(self):
        # Reset the player's hand for a new round
        self.hand = Hand()

    def __str__(self):
        # Return a string representation of the player
        return f"Player: {self.name}, Chips: {self.chips}"

class Dealer(Player):
    def __init__(self):
        # Initialize the dealer
        super().__init__(name="Dealer", chips=0)
        self.show_one_card = True

    def show_hand(self):
        # Display the dealer's hand. Only show one card if 'show_one_card' is True
        if self.show_one_card:
            print("Dealer's Hand: [Hidden],", self.hand.cards[1])
        else:
            print("Dealer's Hand:", self.hand)

    def play_hand(self, deck):
        # Dealer plays their hand, stops after exceeding 17 value
        self.show_one_card = False
        while self.hand.value < 17:
            self.hit(deck)

