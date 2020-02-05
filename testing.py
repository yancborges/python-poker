from deck import deck
from hand import hand

deck = deck()
print(deck)

deck.shuffle()
print(deck)

my_hand = deck.draw(5)
print(my_hand)
print(deck)