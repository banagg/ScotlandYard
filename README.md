# ScotlandYard

## About
1. Computer version for the popular board game [Scotland Yard](https://en.wikipedia.org/wiki/Scotland_Yard_(board_game)).
2. The rules for the game can be viewed [here](https://plentifun.com/rules-to-play-scotland-yard-board-game).

## How to Play
1. The player who wants to play as Mr. X would have to first enter his/her IP address in mr_x_server.py file and then save it.
2. The players playing as the detectives would have to likewise enter their IP address in the det_client.py file and then save it.
3. The player playing as Mr. X would have to first run mr_x_server.py.
4. The detectives would have to then run det_client.py after it is made sure that the mr_x_server.py file is up and running.
5. The players can now play the game, with their turn being invoked only after the player before their turn is finished with his/her turn.
6. The game will continue either until the no. of turns have exhausted or if Mr. X is caught by the detectives.

## Technologies Used
- Python
- Sockets
- PyQt5
- Pickle
- Graph Theory
