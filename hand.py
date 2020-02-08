from utils import higher_from_cards, get_game_name

class hand:


    def __init__(self, cards):

        self.cards = cards
        self.sort()
        self.labels, self.labels_list, self.suits, self.suits_list = self.hand_values()
        self.hand_info = {
            'label_count': self.labels, 
            'labels': self.labels_list,
            'suit_count': self.suits,
            'suits': self.suits_list
        }
        
        self.game_raw = higher_from_cards(self.hand_info, self.cards)
        self.game_value = self.game_raw[2]
        self.game_cards = [str(card) for card in self.game_raw[1]]
        self.game_name = get_game_name(self.game_raw[2])
        self.game = self.mount_game()

    
    def __str__(self):
        return str([str(card) for card in self.cards])
        

    
    def get_info(self):
        return 'Hand: \t{}\nInfo: \t{}'.format(str([str(card) for card in self.cards]), self.hand_info)


    def mount_game(self):
        return '{} - {}'.format(self.game_name, self.game_cards)


    def hand_values(self):

        labels = {}
        labels_list = []
        suits = {}
        suits_list = []

        for card in self.cards:
            if not labels.get(card.label):
                labels[card.label] = {'count': 1, 'content': [card]}
                labels_list.append(card.label)
            else:
                labels[card.label]['count'] += 1
                labels[card.label]['content'].append(card)

            if not suits.get(card.suit):
                suits[card.suit] = {'count': 1, 'content': [card]}
                suits_list.append(card.suit)
            else:
                suits[card.suit]['count'] += 1
                suits[card.suit]['content'].append(card)

        return labels, labels_list, suits, suits_list


    def sort(self):

        count = 0
        lower_index = 0

        while count < len(self.cards):
            lower_index = count
            low_card = self.cards[lower_index]
            for card in self.cards[count:]:
                if card.value < low_card.value:
                    lower_index = self.cards.index(card)
                    low_card = self.cards[lower_index]
            
            dummy = low_card 
            self.cards[lower_index] = self.cards[count]
            self.cards[count] = dummy
            count += 1
        