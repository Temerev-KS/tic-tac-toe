from player import Player
from board import Board


class GameEngine:
    def __init__(self):
        self._players: [Player] = [Player('X'), Player('O')]
        self._board = Board()
        self._game_on = True
        self._current_player: Player | None = None
        self._score_limit = 3
    
    def is_game_on(self):
        return self._game_on
    
    def set_game_off(self):
        self._game_on == False
    
    def repeat_game_input(self):
        repeat_decision = input('Do you you want to play again? \n(press Y or N keys)\n').lower()
        while repeat_decision != 'y' or repeat_decision != 'n':
            repeat_decision = input('Invalid input: please press "Y" key to play again or "N" key to exit\n').lower()
        if repeat_decision == 'y':
            self._game_on == True
        elif repeat_decision == 'n':
            self._game_on == False
    
    @staticmethod
    def show_logo():
        with open('logo', mode='r') as lg:
            askii_logo = lg.read()
        print(askii_logo)
        
    # def reset_board
        
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
        self._board.write_cell(
            *self.ask_for_user_input(),
            value=self._current_player.figure
        )
    
    def show_board(self):
        print(self._board.get_formatted_state())
        
    def check_winning_combo_present(self) -> str | None:
        for combo in self._board.winning_combinations():
            if self._board.cell_not_empty_check(*combo[0]):
                cell_0 = self._board.get_cell_value(*combo[0])
                cell_1 = self._board.get_cell_value(*combo[1])
                cell_2 = self._board.get_cell_value(*combo[2])
                if cell_0 == cell_1 and cell_1 == cell_2:
                    print('#################### kawabunga ####################')
                    return cell_0
                
    def report_round_winner(self,):
        pass

    def check_player_score(self, player):
        if player.show_score() == self._score_limit:
            return True
    
    def check_for_winner(self):
        if self._players[0] > self._players[1]:
            return self._players[0]
        elif self._players[0] < self._players[1]:
            return self._players[1]
        elif self._players[0] == self._players[1]:
            self._score_limit += 1
            return 'draw'
        else:
            return None
            
    def ask_for_user_input(self):
        print(f"{self._current_player.get_name()}, your turn, select the next move")
        column_address = input('Column name (a, b c): ')
        while column_address not in self._board.get_state().keys():
            column_address = input('Invalid column name, please enter correct one  (E.g - a, b, c): ')
        row_address = input('Row number (1, 2, 3): ')
        while row_address not in self._board.get_state()['a'].keys():
            row_address = input('Invalid row number, please enter correct one  (E.g - 1, 2, 3): ')
        return column_address, row_address
    
    @staticmethod
    def result_draw():
        print("Draw")
    
    @staticmethod
    def result_victory(winner):
        print(f'Player {winner}')

    

if __name__ == '__main__':
    pass
