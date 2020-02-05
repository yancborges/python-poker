from utils import higher_from_cards

class hand:


    def __init__(self, cards):

        self.cards = cards
        self.game = higher_from_cards(self.cards)