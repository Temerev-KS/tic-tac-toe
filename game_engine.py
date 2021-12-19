import numpy as np
# ┌ ┐ └ ┘ ├ ┤ ┬ ┴ ┼ │ ─ O X
# TODO: create function to handle console text
"""
┌───┬───┬───┐
│ X │ O │ X │
├───┼───┼───┤
│   │ X │ O │
├───┼───┼───┤
│ O │   │ X │
└───┴───┴───┘

┌───┬───┬───┐
│  │  │  │
├───┼───┼───┤
│  │  │  │
├───┼───┼───┤
│  │  │  │
└───┴───┴───┘
"""


class GameEngine:
    def __init__(self):
        self._players = None
        self._game_going = None
        self.__visual_state = {
            'a': {1: ' ', 2: ' ', 3: ' '},
            'b': {1: ' ', 2: ' ', 3: ' '},
            'c': {1: ' ', 2: ' ', 3: ' '}
        }
        self.__winning_states = [
            (('a', 1), ('a', 2), ('a', 3)), 
            (('b', 1), ('b', 2), ('b', 3)), 
            (('c', 1), ('c', 2), ('c', 3)), 
            (('a', 1), ('b', 1), ('c', 1)), 
            (('a', 2), ('b', 2), ('c', 2)), 
            (('a', 3), ('b', 3), ('c', 3)), 
            (('a', 1), ('b', 2), ('c', 3)),
            (('a', 3), ('b', 2), ('c', 1)),
        ]
        
    def init_empty_field(self):
        self.__visual_state = {'a': {1: ' ', 2: ' ', 3: ' '},
                               'b': {1: ' ', 2: ' ', 3: ' '},
                               'c': {1: ' ', 2: ' ', 3: ' '}}
        
    def show_state(self):
        print(f'    a   b   c  \n'
              f'  ┌───┬───┬───┐\n'
              f'1 │ {self.__visual_state["a"][1]} │ {self.__visual_state["b"][1]} │ {self.__visual_state["c"][1]} │\n'
              f'  ├───┼───┼───┤\n'
              f'2 │ {self.__visual_state["a"][2]} │ {self.__visual_state["b"][2]} │ {self.__visual_state["c"][2]} │\n'
              f'  ├───┼───┼───┤\n'
              f'3 │ {self.__visual_state["a"][3]} │ {self.__visual_state["b"][3]} │ {self.__visual_state["c"][3]} │\n'
              f'  └───┴───┴───┘')
    
    def record_move(self, column, row, value):
        self.__visual_state[column][row] = value
    
    def check_state(self) -> str:
        # Checks if there are any winning combination on the board, and returns symbol of winner combination
        def get_symbol(column, row):  # function to get one of the symbols from the combination
            return self.__visual_state[column][row]
        for state in self.__winning_states:  # loop thru all predetermined "states" (group of coordinates)
            symbol = get_symbol(*state[0])  # get the symbol from the first cell in the state
            if symbol != " " or symbol is not None:  # continue only if cell is not "empty"
                # if second and third symbols are equal - # TODO: Continue this sentence
                if symbol == get_symbol(*state[1]) and symbol == get_symbol(*state[2]):  # if second and third symbols
                    print('kawabunga')
                    return symbol
    
if __name__ == '__main__':
    engine = GameEngine()
    engine.show_state()
    engine.record_move('a', 1, 'X')
    engine.record_move('a', 2, 'X')
    engine.record_move('a', 3, 'X')
    engine.show_state()
    engine.check_state()
