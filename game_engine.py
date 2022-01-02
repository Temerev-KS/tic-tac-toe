from player import Player
from board import Board
import os
# TODO: A ton of refactoring (+ standardise function and variable naming)


class GameEngine:
    def __init__(self):
        self._players: [Player] = [Player('X'), Player('O')]
        self._board = Board()
        self._game_on = True
        self._current_player: Player | None = None
        self._score_limit = 3

    @staticmethod
    def show_logo():
        with open('logo', mode='r') as lg:
            ascii_logo = lg.read()
        print(ascii_logo)

    def display_players_score(self):
        print(f'Score:\n'
              f'{self._players[0].get_name()} : {self._players[0].show_score()}  |  '
              f'{self._players[1].get_name()} : {self._players[1].show_score()}'
              f'\n')

    @staticmethod
    def clear_terminal():
        os.system('cls' if os.name == 'nt' else 'clear')

    def game_loop(self):
        # Main method responsible for the game
        while self._game_on:
            while not self.game_winner_check():
                while not self.round_winner_check():
                    if self.board_has_empty_cells_check():
                        self.change_player()
                        self.move()
                    else:
                        self.round_result_draw()
            self.ask_to_repeat_game()
        print('Good by!')
    
    def ask_to_repeat_game(self):
        repeat_decision = input('Do you you want to play again? \n(press Y or N keys)\n').lower()
        while repeat_decision not in ('y', 'n'):
            repeat_decision = input('Invalid input: please press "Y" key to play again or "N" key to exit\n').lower()
        if repeat_decision == 'y':
            self._game_on = True
            self.reset_game()
        elif repeat_decision == 'n':
            self._game_on = False
    
    def reset_game(self):
        #  Reset everything to the default but keeps the name of the players
        self._board.empty()
        self._score_limit = 3
        for player in self._players:
            player.reset_score()
    
    def name_players(self):
        for index, player in enumerate(self._players):
            user_name = input(f'Enter name for the Player {index + 1}\n')
            while user_name == '':
                self.clear_terminal()
                self.show_logo()
                user_name = input(f'You entered nothing!\n'
                                  f'Please enter name for the Player {index + 1}\n')
            player.set_name(user_name)
        
    def change_player(self):
        if self._current_player is self._players[0]:
            self._current_player = self._players[1]
        else:
            self._current_player = self._players[0]
        
    def move(self):
        self.display_board()
        print(f"\nEnter the next move")
        cell_address = self.ask_for_user_input()
        while self._board.cell_not_empty_check(*cell_address):
            self.display_board()
            print(f'\nSorry sell {cell_address} is not empty, please select a different one')
            cell_address = self.ask_for_user_input()
        self._board.write_cell(*cell_address, value=self._current_player.get_figure())
    
    def display_board(self):
        self.clear_terminal()
        self.show_logo()
        self.display_players_score()
        print(self._board.get_formatted_state())  # Display formatted grid of cells
        print(f"\n{self._current_player.get_figure()}'s: {self._current_player.get_name()}")
        
    def round_winner_check(self) -> bool | None:
        for combo in self._board.winning_combinations():
            if self._board.cell_not_empty_check(*combo[0]):
                cell_0 = self._board.get_cell_value(*combo[0])
                cell_1 = self._board.get_cell_value(*combo[1])
                cell_2 = self._board.get_cell_value(*combo[2])
                if cell_0 == cell_1 and cell_1 == cell_2:
                    self.round_result_victory()
                    return True

    def board_has_empty_cells_check(self):
        return True if self._board.get_empty_cells_count() >= 1 else False
    
    def game_winner_check(self):
        if self._players[0] == self._players[1] and self._players[0].show_score() == self._score_limit:
            self._score_limit += 1
            return False
        elif self._current_player is not None:  # None is the state at the beginning of the game
            if self._current_player.show_score() >= self._score_limit:
                self.game_winner()
                return True
            else:
                return False
        else:
            return False
            
    def ask_for_user_input(self):
        # User must enter cell address as column name and row number in order to make a move
        column_address = input('Enter column name (a, b c): ')
        while column_address not in self._board.get_state().keys():
            self.display_board()
            column_address = input('Invalid column name, please enter correct one  (E.g - a, b, c): ')
        row_address = input('Enter row number (1, 2, 3): ')
        while row_address not in self._board.get_state()['a'].keys():
            self.display_board()
            print(f'Selected column is "{column_address}"')
            row_address = input('Invalid row number, please enter correct one  (E.g - 1, 2, 3): ')
        return column_address, row_address
    
    def round_result_draw(self):
        self._board.empty()
        print("\nDraw!")
        input('\nPress "Enter" to continue: ')
    
    def round_result_victory(self):
        self._current_player.add_score()
        self._board.empty()
        print(f'\nPlayer {self._current_player.get_name()} is victorious!')
        input('\nPress "Enter" to continue: ')
    
    def game_winner(self):
        print(f'\nPlayer {self._current_player.get_name()} won the game!')

    
if __name__ == '__main__':
    pass
