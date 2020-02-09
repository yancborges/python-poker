

def higher_from_cards(hand_info, card_list):

    labels = hand_info['label_count']
    label_list = hand_info['labels']
    suits = hand_info['suit_count']
    suit_list = hand_info['suits']
    
    first_suit = suit_list[0]

    def royal_street_flush():
        game_value = 10
        if not suit_list == [first_suit]:
            return False, [], game_value

        if not label_list == ['10', 'J', 'Q', 'K', 'A']:
            return False, [], game_value

        return True, card_list, game_value

    
    def street_flush():
        game_value = 9
        if len(label_list) < 5:
            return False, [], game_value
        for label in label_list[1:]:
            if not get_label_value(label)[1] == get_label_value(label_list[label_list.index(label) - 1])[0] + 1:
                return False, [], game_value
        
        if not suit_list == [first_suit]:
            return False, [], game_value
        
        return True, card_list, game_value


    def four():
        game_value = 8
        for key in labels:
            if labels[key]['count'] == 4:
                return True, labels[key]['content'], game_value
        return False, [], game_value
    

    def full_house():
        game_value = 7
        three = False
        pair = False
        for key in labels:
            if labels[key]['count'] == 3:
                three = True
            if labels[key]['count'] == 2:
                pair = True

        if three and pair:
            return True, card_list, game_value
        return False, [], game_value


    def flush():
        game_value = 6
        if suit_list == [first_suit]:
            return True, card_list, game_value
        return False, [], game_value


    def straight():
        game_value = 5
        if len(label_list) < 5:
            return False, [], game_value
        for label in label_list[1:]:
            #if not get_label_value(label)[0] in get_label_value(label_list[label_list.index(label) - 1]) + 1:
            if not get_label_value(label)[1] == get_label_value(label_list[label_list.index(label) - 1])[0] + 1:
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
        'A': [14, 1],
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
    
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
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


def compare_games(table_players):

    _sorted = []
    count = 0
    while count < len(table_players):
        winner_index = count
        winner_obj = table_players[winner_index]
        winner_hand = winner_obj.hand
        for plr in table_players[count:]:
            h = plr.hand
            if h.game_value == winner_hand.game_value:
                h_values = [get_label_value(h_card)[0] for h_card in h.game_labels_list]
                w_values = [get_label_value(w_card)[0] for w_card in winner_hand.game_labels_list]

                if sum(h_values) > sum(w_values):
                    winner_index = table_players.index(plr)
                    winner_obj = plr
                    winner_hand = winner_obj.hand

                elif sum(h_values) == sum(w_values):
                    if plr != winner_obj:
                        plr.splitted = True
                        winner_obj.splitted = True
            
            elif h.game_value > winner_hand.game_value:
                winner_index = table_players.index(plr)
                winner_obj = plr
                winner_hand = winner_obj.hand

        _sorted.append(winner_obj)
        count = len(_sorted)

    return _sorted
