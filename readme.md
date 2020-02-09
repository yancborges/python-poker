# Python poker

## Code map:

| File | Quick Description | Classes dependencies |
| ------------------- | ------------------- |
|  Card |  Card object | None   |
| Deck | A list with each card | Card |
|  Hand |  List of cards | Card |
| Player | Info about person holding the cards | Hand |
| Testing | Some auto-test code, with mocks for each game | None |
| Main | File that runs the game with 5 players and tells who's the winner |


## Logic:

Criter for winner hand: https://www.pokerstars.com/poker/games/rules/hand-rankings/?no_redirect=1

## How to run:

The main.py file runs everything automatically,
but if you want to set the number of players, you can change
the argument passed to the function 'start_game'


## Class description

### Deck
    - Description: Mounts a deck with the list of 52 cards, all unique.
    - Functions:
        - my_deck = deck(): Creates a new deck with 52 cards
        - my_deck.shuffle(): Shuffles the deck
        - my_deck.draw(<N>): Draws N cards from the deck
        - my_deck.restore(): Resets deck


### Hand
    - Description: Recieves a list of cards, and get infos about the cards within
    - Functions:
        - my_hand = hand(<card_list>): Creates a hand with the cards in a list
        - my_hand.get_info(): Returns some util info like number of each suits of the highest game found
            * Note: These data are used mainly to compare and find games in the hand

### Player
    - Description: Sets a player with a hand of cards
    - Functions:
        - me = player(<hand>): Instances a new player with a random name    