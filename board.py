class Board:
    def __init__(self):
        self.__state = {
            'a': {'1': ' ', '2': ' ', '3': ' '},
            'b': {'1': ' ', '2': ' ', '3': ' '},
            'c': {'1': ' ', '2': ' ', '3': ' '}
        }
        self.__winning_combinations = [
            (('a', '1'), ('a', '2'), ('a', '3')),
            (('b', '1'), ('b', '2'), ('b', '3')),
            (('c', '1'), ('c', '2'), ('c', '3')),
            (('a', '1'), ('b', '1'), ('c', '1')),
            (('a', '2'), ('b', '2'), ('c', '2')),
            (('a', '3'), ('b', '3'), ('c', '3')),
            (('a', '1'), ('b', '2'), ('c', '3')),
            (('a', '3'), ('b', '2'), ('c', '1')),
        ]
    
    def winning_combinations(self):
        return self.__winning_combinations
        
    def empty(self):
        self.__state = {'a': {'1': ' ', '2': ' ', '3': ' '},
                        'b': {'1': ' ', '2': ' ', '3': ' '},
                        'c': {'1': ' ', '2': ' ', '3': ' '}}
    
    def get_formatted_state(self):
        formatted_state = str(f'    a   b   c  \n'
                              f'  ┌───┬───┬───┐\n'
                              f'1 │ {self.__state["a"]["1"]} │ {self.__state["b"]["1"]} │ {self.__state["c"]["1"]} │\n'
                              f'  ├───┼───┼───┤\n'
                              f'2 │ {self.__state["a"]["2"]} │ {self.__state["b"]["2"]} │ {self.__state["c"]["2"]} │\n'
                              f'  ├───┼───┼───┤\n'
                              f'3 │ {self.__state["a"]["3"]} │ {self.__state["b"]["3"]} │ {self.__state["c"]["3"]} │\n'
                              f'  └───┴───┴───┘')
        return formatted_state
    
    def get_state(self):
        return self.__state
    
    def get_cell_value(self, column, row) -> str | None:
        return self.__state[column][row]
    
    def write_cell(self, column: str, row: str, value: str):
        self.__state[column][row] = value
    
    def cell_not_empty_check(self, column, row) -> bool:
        if self.__state[column][row] == ' ' or self.__state[column][row] is None:
            return False
        else:
            return True

