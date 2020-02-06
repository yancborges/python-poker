from utils import get_card_list
from random import shuffle
from copy import deepcopy
from card import card

class deck:


    def __init__(self):
        self.deck_list = self.load_deck()
        self.deck_copy = deepcopy(self.deck_list)
        self.size = len(self.deck_list)


    def __str__(self):
        return 'Number of cards: {}\nCurrent on deck: {}\nCard list: {}'.format(
            len(self.deck_copy), len(self.deck_list), [str(card) for card in self.deck_list]
        )


    def load_deck(self):
        
        card_list = []
        raw_list = get_card_list()
        
        for _card in raw_list:
            card_obj = card(_card['label'], _card['suit'], _card['value'])
            card_list.append(card_obj)

        return card_list


    def shuffle(self):
        shuffle(self.deck_list)


    def draw(self, number):

        if len(self.deck_list) < number:
            raise ValueError('Erro, numero de cartas insuficiente')
        
        drew = self.deck_list[:number]
        del self.deck_list[:number]

        self.size = len(self.deck_list)

        return drew


    def restore(self):
        self.deck_list = deepcopy(self.deck_copy)

