from player import Player
from board import Board


class GameEngine:
    def __init__(self):
        self._players: [Player] = [Player('X'), Player('O')]
        self._game_going = None
        self._current_player: Player | None = None
        self.score_limit = 3
        self.board = Board()
        
    def name_players(self):
        for index, player in enumerate(self._players):
            user_name = input(f'Enter name for the Player {index + 1}\n')
            player.set_name(user_name)
        
    def change_player(self):
        if self._current_player is self._players[0]:
            self._current_player = self._players[1]
        else:
            self._current_player = self._players[0]
        
    def move(self):
        self.board.write_cell(
            *self.ask_for_user_input(),
            value=self._current_player.figure
        )
    
    def show_board(self):
        print(self.board.get_formatted_state())
        
    def check_winning_combo_present(self) -> str | None:
        for combo in self.board.winning_combinations():
            if self.board.cell_not_empty_check(*combo[0]):
                cell_0 = self.board.get_cell_value(*combo[0])
                cell_1 = self.board.get_cell_value(*combo[1])
                cell_2 = self.board.get_cell_value(*combo[2])
                if cell_0 == cell_1 and cell_1 == cell_2:
                    print('#################### kawabunga ####################')
                    return cell_0

    def check_player_score(self, player):
        if player.show_score() == self.score_limit:
            return True
    
    def check_for_winner(self):
        if self._players[0] > self._players[1]:
            return self._players[0]
        elif self._players[0] < self._players[1]:
            return self._players[1]
        elif self._players[0] == self._players[1]:
            self.score_limit += 1
        else:
            return None
            
    def ask_for_user_input(self):
        print(f"{self._current_player.get_name()}, your turn, select the next move")
        column_address = input('Column name (a, b c): ')
        while column_address not in self.board.get_state().keys():
            column_address = input('Invalid column name, please enter correct one  (E.g - a, b, c): ')
        row_address = input('Row number (1, 2, 3): ')
        while row_address not in self.board.get_state()['a'].keys():
            row_address = input('Invalid row number, please enter correct one  (E.g - 1, 2, 3): ')
        return column_address, row_address
    
    @staticmethod
    def result_draw():
        print("Draw")
    
    @staticmethod
    def result_victory(winner):
        print(f'Player {winner}')
    
    def result_loss(self):
        pass
    

if __name__ == '__main__':
    pass
