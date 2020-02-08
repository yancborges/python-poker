from deck import deck
from hand import hand
from card import card
from utils import compare_games, get_game_name

def cards_test(test=None):

    def mock_highcard():
        return [[
            card('A','Hearts', 14),
            card('2','Spades', 0),
            card('3','Spades', 1),
            card('4','Spades', 2),
            card('5','Spades', 3),
        ], 1, get_game_name(1)]

    def mock_pair():
        return [[
            card('2','Spades', 0),
            card('2','Clubs', 0),
            card('3','Spades', 1),
            card('4','Spades', 2),
            card('5','Spades', 3),
        ], 2, get_game_name(2)]

    def mock_twopairs():
        return [[
            card('2','Spades', 0),
            card('2','Clubs', 0),
            card('3','Spades', 1),
            card('3','Clubs', 1),
            card('4','Spades', 2),
        ], 3, get_game_name(3)]

    def mock_three():
        return [[
            card('2','Spades', 0),
            card('2','Clubs', 0),
            card('2','Hearts', 0),
            card('3','Spades', 1),
            card('4','Spades', 2),
        ], 4, get_game_name(4)]

    def mock_straight():
        return [[
            card('2','Spades', 0),
            card('3','Spades', 1),
            card('4','Spades', 2),
            card('5','Clubs', 3),
            card('6','Spades', 4),
        ], 5, get_game_name(5)]

    def mock_flush():
        return [[
            card('2','Spades', 0),
            card('3','Spades', 1),
            card('4','Spades', 2),
            card('5','Spades', 3),
            card('A','Spades', 14),
        ], 6, get_game_name(6)]

    def mock_fullhouse():
        return [[
            card('2','Spades', 0),
            card('2','Clubs', 0),
            card('3','Clubs', 1),
            card('3','Spades', 1),
            card('3','Hearts', 1),
        ], 7, get_game_name(7)]

    def mock_four():
        return [[
            card('2','Spades', 0),
            card('2','Clubs', 0),
            card('2','Diamonds', 0),
            card('2','Hearts', 0),
            card('3','Spades', 1),
        ], 8, get_game_name(8)]

    def mock_street():
        return [[
            card('2','Spades', 0),
            card('3','Spades', 1),
            card('4','Spades', 2),
            card('5','Spades', 3),
            card('6','Spades', 4),
        ], 9, get_game_name(9)]

    def mock_royal():
        return [[
            card('10','Spades', 8),
            card('J','Spades', 9),
            card('Q','Spades', 10),
            card('K','Spades', 11),
            card('A','Spades', 12),
        ], 10, get_game_name(10)]

    test = [
        mock_highcard(),
        mock_pair(),
        mock_twopairs(),
        mock_three(),
        mock_straight(),
        mock_flush(),
        mock_fullhouse(),
        mock_four(),
        mock_street(),
        mock_royal()
    ]

    failed_list = []
    ok_list = []

    for mock in test:
        mock_game = mock[0]
        mock_value = mock[1]
        mock_name = mock[2]
        test_hand = hand(mock[0])
        print('\nTesting {}...'.format(mock_name))
        if test_hand.game_value == mock_value:
            ok_list.append(mock_name)
        else:
            failed_list.append(mock_name)

    print('\n\nFinished test:')
    print('Passed:', ok_list)
    print('Failed', failed_list)

def random_test():

    my_deck = deck()
    my_deck.shuffle()

    hands = []
    while my_deck.size >= 5:
        my_hand = hand(my_deck.draw(5))
        hands.append(my_hand)

        print(my_hand)
        print(my_hand.game)
        print('\n')

cards_test()

"""
deck = deck()
#print(deck)
#print('\n\n')

deck.shuffle()
#print(deck)
#print('\n\n')

my_hand = hand(deck.draw(5))
#print(my_hand)
#print('\n\n')

#print(deck)
#print('\n\n')

print(my_hand)
print(my_hand.game)
"""