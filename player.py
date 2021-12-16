class Player:
    def __init__(self):
        self._player_name = None
        self._victories = 0
    
    def __str__(self):
        if self._player_name is None:
            return 'Undefined Player'
        else:
            return f'Player {self._player_name}'
        
    def __repr__(self):
        if self._player_name is None:
            return 'Undefined Player'
        else:
            return f'Player {self._player_name}'
        
    def set_name(self, new_name=None):
        if new_name is not None:
            self._player_name = new_name
    
    @staticmethod
    def add_score(self):
        self._victories += 1
    
    def show_score(self):
        return self._victories

    def make_move(self):
        pass
        # TODO: figure out if this method is needed at all here
    

if __name__ == '__main__':
    pass
