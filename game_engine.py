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
        self.__game_state = None
        self.__game_visual_state = None
        
    def init_empty_field(self):
        self._game_going = True
        self.__game_state = np.full((3, 3), 0)
        self.__game_visual_state = '‗‗‗'
        
    
