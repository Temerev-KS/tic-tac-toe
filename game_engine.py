class GameEngine:
    def __init__(self):
        self._players = []
        self._game_going = None
        self._current_player = None
        self.score_limit = 3
        self.__state = {
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
        self.__state = {'a': {1: ' ', 2: ' ', 3: ' '},
                        'b': {1: ' ', 2: ' ', 3: ' '},
                        'c': {1: ' ', 2: ' ', 3: ' '}}
        
    def show_state(self):
        print(f'    a   b   c  \n'
              f'  ┌───┬───┬───┐\n'
              f'1 │ {self.__state["a"][1]} │ {self.__state["b"][1]} │ {self.__state["c"][1]} │\n'
              f'  ├───┼───┼───┤\n'
              f'2 │ {self.__state["a"][2]} │ {self.__state["b"][2]} │ {self.__state["c"][2]} │\n'
              f'  ├───┼───┼───┤\n'
              f'3 │ {self.__state["a"][3]} │ {self.__state["b"][3]} │ {self.__state["c"][3]} │\n'
              f'  └───┴───┴───┘')
    
    def record_move(self, column: str, row: int, value: str):
        """
        Writes value to __state, in order to store current player move.
        eg. ('a', 2, )
        """
        self.__state[column][row] = value
    
    def check_state(self) -> str:
        # Checks if there are any winning combination on the board, and returns symbol of winner combination
        def get_symbol(column, row):  # function to get one of the symbols from the combination
            return self.__state[column][row]
        for state in self.__winning_states:  # loop thru all predetermined "states" (group of coordinates)
            symbol = get_symbol(*state[0])  # get the symbol from the first cell in the state
            if symbol != " " or symbol is not None:  # continue only if cell is not "empty"
                # if second and third symbols are equal - returns that symbol
                if symbol == get_symbol(*state[1]) and symbol == get_symbol(*state[2]):  # if second and third symbols
                    print('kawabunga')
                    return symbol
                
    def change_player(self):
        for player in self._players:
            if self._current_player != player:
                self._current_player = player
                
    def check_player_score(self, player):
            if player.show_score() == self.score_limit:
                return True
    
    def compare_players_score(self):
        if self._players[0] > self._players[1]:
            return self._players[0]
        
        elif self._players[0] > self._players[1]:
            return self._players[1]
            
        elif self._players[0] == self._players[1]:
            self.score_limit += 1
            
    def result_draw(self):
        pass
    
    def result_victory(self):
        pass
    
    def result_loss(self):
        pass
    

if __name__ == '__main__':
    engine = GameEngine()
    engine.show_state()
    engine.record_move('a', 1, 'X')
    engine.record_move('a', 2, 'X')
    engine.record_move('a', 3, 'X')
    engine.show_state()
    engine.check_state()
