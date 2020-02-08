from hand import hand
from player import player
from deck import deck
from utils import compare_games

deck = deck()
deck.shuffle()


def start_game(players):

    table = []
    for count in range(players):
        plr = player(hand(deck.draw(5)))
        table.append(plr)

        print(plr, plr.hand.game_cards)

    table = compare_games(table)
    winner = table[0]
    print('\nWinner: {} - {} - {}'.format(winner.name, winner.hand.game_name, winner.hand.game_cards))


start_game(5)