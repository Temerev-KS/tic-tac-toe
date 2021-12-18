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
        self.__state = np.full((3, 3), 0)
        self.__visual_state = {'a': {1: ' ', 2: ' ', 3: ' '},
                               'b': {1: ' ', 2: ' ', 3: ' '},
                               'c': {1: ' ', 2: ' ', 3: ' '}}
        self.exx_player = None
        self.oos_player = None
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
        self._game_going = True
        self.__state = np.full((3, 3), 0)
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
    
    def check_move(self):
        pass
    
    def check_state(self):
        def get_symbol(column, row):
            return self.__visual_state[column][row]
        for state in self.__winning_states:
            symbol = get_symbol(*state[0])
            if symbol == get_symbol(*state[1]) and symbol == get_symbol(*state[2]):
                print('kawabunga')
    
    def v1(self):
        if self.__visual_state['a'][1] == 'X' and self.__visual_state['a'][2] and self.__visual_state['a'][3] == 'X':
            return True
        else:
            return False

    
    
if __name__ == '__main__':
    engine = GameEngine()
    engine.show_state()
    engine.record_move('a', 1, 'X')
    engine.record_move('a', 2, 'X')
    engine.record_move('a', 3, 'X')
    engine.show_state()
    engine.check_state()
