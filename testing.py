from deck import deck
from hand import hand

deck = deck()
deck.shuffle()

hands = []
while deck.size >= 5:
    my_hand = hand(deck.draw(5))
    hands.append(my_hand)

    print(my_hand)
    print(my_hand.game)
    print('\n')

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