"""

Main idea is to use different numbers to store the game state.
There are 8 possible combinations.
We will assign first player value of 1
second player will have value of 4
After each move we are going to check the state of the game.
We are going to do that by adding 3 numbers in each possible combination.
If sum of any combination will resul in 3 or 12 - we have a winner.
3 - player one won
12 - player two won.

We will store the game state in two forms:
    one is the numerical state, to calculate the winner
    another is text state, to be printed in the console

Player will have to enter the row and column ID to make a move (similar to a chess game).

Wen player makes a move - we change 'ACTIVE PLAYER' variable that will define witch number and character to store.
Active player will also be used to display in the console what player is currently making a move.


"""

from player import Player
from game_engine import GameEngine


def func():
    engine = GameEngine()
    # player_1 = Player()
    # player_1.set_name('Ner\'zhul')
    # player_2 = Player()
    # player_2.set_name('Thrall')
    # print(player_1)
    # print(player_2)
    engine.init_players()
    engine.name_players()
    engine.change_player()
    engine.show_state()
    engine.move()
    engine.show_state()
    
    

if __name__ == '__main__':
    func()
