class card:


    def __init__(self, label, suit, value):

        self.label = label
        self.suit = suit
        self.abr_suit = self.suit_shorter()
        self.value = value


    def __str__(self):
        return '{}{}'.format(self.label, self.abr_suit)


    def suit_shorter(self):
        return self.suit[0].upper()


    

