class Board:
    def __init__(self):
        self._state = {
            'a': {'1': ' ', '2': ' ', '3': ' '},  # Grid 3x3 with named columns and numbered rows
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
        self._cells_left = 9  # Keeps track of empty cells (max 9 min 0)
    
    def cell_not_empty_check(self, column, row) -> bool:
        """False if cell is empty, True if cell is occupied"""
        if self._state[column][row] == ' ' or self._state[column][row] is None:
            return False
        else:
            return True
        
    def reset(self):
        """Reset board to the initial state"""
        self._state = {
            'a': {'1': ' ', '2': ' ', '3': ' '},
            'b': {'1': ' ', '2': ' ', '3': ' '},
            'c': {'1': ' ', '2': ' ', '3': ' '}
        }
        self._cells_left = 9

    def get_cell_value(self, column, row) -> str | None:
        """Returns value of the cell at specified coordinates"""
        return self._state[column][row]

    def get_empty_cells_count(self) -> int:
        """Getter of empty cells counter (_cells_left)"""
        return self._cells_left
   
    def get_formatted_state(self) -> str:
        """
        Getter of formatted grid of cells with values that looks more or less like square
             a     b     c
          ┌─────┬─────┬─────┐
        1 │     │     │  0  │
          ├─────┼─────┼─────┤
        2 │     │  X  │     │
          ├─────┼─────┼─────┤
        3 │     │     │     │
          └─────┴─────┴─────┘
        """
        pretty_state = (
            f'     a     b     c  \n'
            f'  ┌─────┬─────┬─────┐\n'
            f'1 │  {self._state["a"]["1"]}  │  {self._state["b"]["1"]}  │  {self._state["c"]["1"]}  │\n'
            f'  ├─────┼─────┼─────┤\n'
            f'2 │  {self._state["a"]["2"]}  │  {self._state["b"]["2"]}  │  {self._state["c"]["2"]}  │\n'
            f'  ├─────┼─────┼─────┤\n'
            f'3 │  {self._state["a"]["3"]}  │  {self._state["b"]["3"]}  │  {self._state["c"]["3"]}  │\n'
            f'  └─────┴─────┴─────┘'
        )
        return pretty_state
    
    def get_state(self) -> dict:
        """Getter of raw grid values"""
        return self._state

    def write_cell(self, column: str, row: str, value: str):
        """Sets value of specified cell with provided value, reduces counter of empty cells by 1"""
        self._state[column][row] = value
        self._cells_left -= 1

    def winning_combinations(self) -> [dict]:
        """Getter of _winning_combinations list"""
        return self._winning_combinations
    

if __name__ == '__main__':
    pass
