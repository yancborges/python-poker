def higher_from_cards(hand_info, card_list):

    labels = hand_info['label_count']
    label_list = hand_info['labels']
    suits = hand_info['suit_count']
    suit_list = hand_info['suits']

    label_list.sort()
    suit_list.sort()
    
    first_suit = suit_list[0]

    def royal_street_flush():
        game_value = 10
        if not suit_list == [first_suit] * 5:
            return False, [], game_value

        if not label_list == ['10', 'J', 'Q', 'K', 'A']:
            return False, [], game_value

        return True, card_list, game_value

    
    def street_flush():
        game_value = 9
        for label in label_list[1:]:
            if not get_label_value(label)[0] == get_label_value(label_list[label_list.index(label) - 1])[1]:
                return False, [], game_value
        
        if not suit_list == [first_suit] * 5:
            return False, [], game_value
        
        return True, card_list, game_value


    def four():
        game_value = 8
        for key in labels:
            if labels[key]['count'] == 4:
                return True, labels[key]['content']
        return False, [], game_value
    

    def full_house():
        game_value = 7
        for key in labels:
            if not labels[key]['count'] == 3:
                return False, [], game_value
            if not labels[key]['count'] == 2:
                return False, [], game_value

        return True, card_list, game_value


    def flush():
        game_value = 6
        if suit_list == [first_suit] * 5:
            return True, card_list, game_value
        return False, [], game_value


    def straight():
        game_value = 5
        for label in label_list[1:]:
            #if not get_label_value(label)[0] in get_label_value(label_list[label_list.index(label) - 1]) + 1:
            if not get_label_value(label)[0] == get_label_value(label_list[label_list.index(label) - 1])[1]:
                return False, [], game_value
        return True, card_list, game_value


    def three():
        game_value = 4
        for key in labels:
            if labels[key]['count'] == 3:
                return True, labels[key]['content'], game_value
        return False, [], game_value


    def two_pairs():
        game_value = 3
        pair_count = 0
        matched = []
        for key in labels:
            if labels[key]['count'] == 2:
                pair_count += 1
                matched += labels[key]['content']

        if pair_count == 2:
            return True, matched, game_value
        return False, [], game_value


    def pair():
        game_value = 2
        for key in labels:
            if labels[key]['count'] == 2:
                return True, labels[key]['content'], game_value
        return False, [], game_value
    

    def high_card():
        game_value = 1
        return True, labels[label_list[-1]]['content'], game_value


    games = [
        royal_street_flush(),
        street_flush(),
        four(),
        full_house(),
        flush(),
        straight(),
        three(),
        two_pairs(),
        pair(),
        high_card()
    ]


    for comb in games:
        if comb[0]:
            return comb
    

def get_game_name(value):

    games = {
        10: 'Royal street flush',
        9: 'Street flush',
        8: 'Four of a kind',
        7: 'Full house',
        6: 'Flush',
        5: 'Straight',
        4: 'Three of a kind',
        3: 'Two pairs',
        2: 'Pair',
        1: 'High card'
    }

    return games[value]

def get_label_value(label):

    _dict = {
        'A': [1, 14],
        '2': [2, 2],
        '3': [3, 3],
        '4': [4, 4],
        '5': [5, 5],
        '6': [6, 6],
        '7': [7, 7],
        '8': [8, 8],
        '9': [9, 9],
        '10': [10, 10],
        'J': [11, 11],
        'Q': [12, 12],
        'K': [13, 13]
    }

    return _dict[label]



def get_card_list():

    # A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K
    # D(iamonds), S(pades), H(earts), C(lubs)
    
    values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    suits = ['Diamonds', 'Spades', 'Hearts', 'Clubs']
    mounted_deck = []

    for _value in values:
        for _suit in suits:

            current_card = {}
            current_card['label'] = _value
            current_card['suit'] = _suit
            current_card['value'] = values.index(_value)

            mounted_deck.append(current_card)

    return mounted_deck

