from hand import hand
from player import player
from deck import deck
from utils import compare_games

my_deck = deck()
my_deck.shuffle()


def start_game(players):

    table = []
    for count in range(players):
        plr = player(hand(my_deck.draw(5)))
        table.append(plr)

        print(plr, plr.hand.game_cards)

    table = compare_games(table)
    
    winner = table[0]
    if winner.splitted:
        winner_table = splitted_pot(table)
        print('\nPot splitted!')
        print('Winners:\n')
        for plr in winner_table:
            print('Player: {} - {} - {}'.format(plr.name, plr.hand.game_name, plr.hand.game_cards))    
    else:
        print('\nWinner: {} - {} - {}'.format(winner.name, winner.hand.game_name, winner.hand.game_cards))


def splitted_pot(table):
    winner_table = []
    for plr in table:
        if plr.splitted == True:
            if plr not in winner_table:
                winner_table.append(plr)
        else:
            break

    return winner_table


start_game(5)