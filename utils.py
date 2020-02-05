def higher_from_cards(card_list):

    return 0


def get_card_list():

    # A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K
    # D(iamonds), S(pades), H(earts), C(lubs)
    
    values = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
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

