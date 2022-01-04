from functools import total_ordering


@total_ordering  # for ease of comparing two players
class Player:
    def __init__(self, fig=None):
        self._player_name = None
        self._victories = 0
        self._figure = fig if fig is not None else None  # 'X' or '0' but can be anything :)
    
    def __str__(self) -> str:
        if self._player_name is None:
            return 'Undefined Player'
        else:
            return f'Player {self._player_name}, Score: {self._victories}.'
        
    def __repr__(self) -> str:
        if self._player_name is None:
            return 'Undefined Player'
        else:
            return f'Player {self._player_name}'

    def __eq__(self, other) -> bool:
        return self._victories == other.get_score()

    def __lt__(self, other) -> bool:
        return self._victories <= other.get_score()
    # Total ordering will take care of the rest comparison methods

    def add_score(self):
        self._victories += 1
        
    def get_figure(self) -> str:
        """Getter of players figure (X or 0)"""
        return self._figure
    
    def get_name(self) -> str:
        return self._player_name
    
    def get_score(self) -> int:
        """Getter of the player's victories counter"""
        return self._victories
    
    def reset_score(self):
        self._victories = 0
    
    def set_name(self, new_name=None):
        """Sets player name, provides explicit error if name is not provided"""
        if new_name is not None:
            self._player_name = new_name
        else:
            return ValueError('No value for the new_name in set name')
    

if __name__ == '__main__':
    pass
