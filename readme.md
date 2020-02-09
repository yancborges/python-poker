# Python poker

### Code map:

| File | Quick Description | Classes dependencies |
| ------------------- | ------------------- |
|  Card |  Card object | None   |
|  Hand |  List of cards | Card |
| Player | Info about person holding the cards | Hand |
| Testing | Some auto-test code, with mocks for each game | None |
| Main | File that runs the game with 5 players and tells who's the winner |


### Logic:

Criter for winner hand: https://www.pokerstars.com/poker/games/rules/hand-rankings/?no_redirect=1

### How to run:

The main.py file runs everything automatically,
but if you want to set the number of players, you can change
the argument passed to the function 'start_game'