class Board:
    def __init__(self):
        self._state = {
            'a': {'1': ' ', '2': ' ', '3': ' '},
            'b': {'1': ' ', '2': ' ', '3': ' '},
            'c': {'1': ' ', '2': ' ', '3': ' '}
        }
        self._winning_combinations = [
            (('a', '1'), ('a', '2'), ('a', '3')),  # Vertical
            (('b', '1'), ('b', '2'), ('b', '3')),  # Vertical
            (('c', '1'), ('c', '2'), ('c', '3')),  # Vertical
            (('a', '1'), ('b', '1'), ('c', '1')),  # Horizontal
            (('a', '2'), ('b', '2'), ('c', '2')),  # Horizontal
            (('a', '3'), ('b', '3'), ('c', '3')),  # Horizontal
            (('a', '1'), ('b', '2'), ('c', '3')),  # Diagonal
            (('a', '3'), ('b', '2'), ('c', '1')),  # Diagonal
        ]
        self._cells_left = 9
    
    def winning_combinations(self):
        return self._winning_combinations
        
    def empty(self):
        self._state = {
            'a': {'1': ' ', '2': ' ', '3': ' '},
            'b': {'1': ' ', '2': ' ', '3': ' '},
            'c': {'1': ' ', '2': ' ', '3': ' '}
        }
        self._cells_left = 9
   
    def get_formatted_state(self):
        pretty_state = (f'     a     b     c  \n'
                        f'  ┌─────┬─────┬─────┐\n'
                        f'1 │  {self._state["a"]["1"]}  │  {self._state["b"]["1"]}  │  {self._state["c"]["1"]}  │\n'
                        f'  ├─────┼─────┼─────┤\n'
                        f'2 │  {self._state["a"]["2"]}  │  {self._state["b"]["2"]}  │  {self._state["c"]["2"]}  │\n'
                        f'  ├─────┼─────┼─────┤\n'
                        f'3 │  {self._state["a"]["3"]}  │  {self._state["b"]["3"]}  │  {self._state["c"]["3"]}  │\n'
                        f'  └─────┴─────┴─────┘')
        return pretty_state
    
    def get_state(self):
        return self._state
    
    def get_cell_value(self, column, row) -> str | None:
        return self._state[column][row]
    
    def write_cell(self, column: str, row: str, value: str):
        self._state[column][row] = value
        self._cells_left -= 1
    
    def cell_not_empty_check(self, column, row) -> bool:  # True if cell is occupied
        if self._state[column][row] == ' ' or self._state[column][row] is None:
            return False
        else:
            return True
    
    def get_empty_cells_count(self):
        return self._cells_left
