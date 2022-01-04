from player import Player
from board import Board
import os


class GameEngine:
    def __init__(self):
        self._players: [Player] = [Player('X'), Player('O')]
        self._board = Board()
        self._game_on = True
        self._current_player: Player | None = None
        self._score_limit = 3
    
    def ask_for_user_input(self) -> (str, str):
        """User must enter cell address as column name and row number in order to make a move"""
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
    
    def ask_to_repeat_game(self):
        """Ask user weather to play again or exit the game"""
        repeat_decision = input('Do you you want to play again? \n(press Y or N keys)\n').lower()
        while repeat_decision not in ('y', 'n'):
            repeat_decision = input('Invalid input: please press "Y" key to play again or "N" key to exit\n').lower()
        if repeat_decision == 'y':
            self._game_on = True
            self.reset_game()
        elif repeat_decision == 'n':
            self._game_on = False
    
    def board_has_empty_cells_check(self) -> bool:
        return True if self._board.get_empty_cells_count() >= 1 else False
    
    @staticmethod
    def clear_terminal():
        """Clears terminal window (cross platform)"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def change_player(self):
        """
        Switches player to a different one at the end of the move,
        and sets current player at the at the first game. Winner gets to be second after a round victory
        """
        if self._current_player is self._players[0]:
            self._current_player = self._players[1]
        else:
            self._current_player = self._players[0]
    
    def display_board(self):
        """Clear window and display (from top to bottom):
        logo, current score, state of the board, and current player name and his figure"""
        self.clear_terminal()
        self.display_logo()
        self.display_players_score()
        print(self._board.get_formatted_state())  # Display formatted grid of cells
        print(f"\n{self._current_player.get_figure()}'s: {self._current_player.get_name()}")
    
    @staticmethod
    def display_logo():
        """Print ASCII ART type of logo to the console"""
        with open('logo', mode='r') as lg:
            ascii_logo = lg.read()
        print(ascii_logo)
    
    def display_players_score(self):
        """Print score of both player's to the console"""
        print(f'Score:\n'
              f'{self._players[0].get_name()} : {self._players[0].get_score()}  |  '
              f'{self._players[1].get_name()} : {self._players[1].get_score()}'
              f'\n')

    def game_winner_check(self) -> bool:
        """
        Checks if anyone won the whole game by comparing players score against the set score limit.
        Adds another round if the scores of players are equal and score limit is reached.
        """
        if self._players[0] == self._players[1] and self._players[0].get_score() == self._score_limit:
            self._score_limit += 1
            return False
        elif self._current_player is not None:  # None is the state at the beginning of the game
            if self._current_player.get_score() >= self._score_limit:
                self.game_winner()
                return True
            else:
                return False
        else:
            return False
    
    def game_loop(self):
        """Main method responsible for the game"""
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

    def game_winner(self):
        """Prints to the console formatted string with the name of the winner"""
        print(f'\nPlayer {self._current_player.get_name()} won the game!')
    
    def reset_game(self):
        #  Reset everything to the default but keeps the name of the players
        self._board.reset()
        self._score_limit = 3
        for player in self._players:
            player.reset_score()
        
    def move(self):
        """
        Player makes a move with this method.
        Asks for coordinates to the desired cell, checks that it's empty, and writes players figure to it.
        """
        self.display_board()
        print(f"\nEnter the next move")
        cell_address = self.ask_for_user_input()
        while self._board.cell_not_empty_check(*cell_address):
            self.display_board()
            print(f'\nSorry sell {cell_address} is not empty, please select a different one')
            cell_address = self.ask_for_user_input()
        self._board.write_cell(*cell_address, value=self._current_player.get_figure())
    
    def name_players(self):
        """Assign names to the players"""
        for index, player in enumerate(self._players):
            user_name = input(f'Enter name for the Player {index + 1}\n')
            while user_name == '':
                self.clear_terminal()
                self.display_logo()
                user_name = input(f'You entered nothing!\n'
                                  f'Please enter name for the Player {index + 1}\n')
            player.set_name(user_name)

    def round_result_draw(self):
        """
        Print to the console that round resulted with draw, resets board for the next round.
        Wait for user to press Enter to continue.
        """
        self._board.reset()
        print("\nDraw!")
        input('\nPress "Enter" to continue: ')
        
    def round_result_victory(self):
        """
        Print to the console that current player (prints his name) won this round, resets board for the next round.
        Wait for user to press Enter to continue.
        """
        self._current_player.add_score()
        self._board.reset()
        print(f'\nPlayer {self._current_player.get_name()} is victorious!')
        input('\nPress "Enter" to continue: ')
        
    def round_winner_check(self) -> bool | None:
        """
        Check for winner of the round by checking all possible winning combinations.
        Call method to announce a winner if one combination matches current state of the board
        """
        for combo in self._board.winning_combinations():
            if self._board.cell_not_empty_check(*combo[0]):
                cell_0 = self._board.get_cell_value(*combo[0])
                cell_1 = self._board.get_cell_value(*combo[1])
                cell_2 = self._board.get_cell_value(*combo[2])
                if cell_0 == cell_1 and cell_1 == cell_2:
                    self.round_result_victory()
                    return True


if __name__ == '__main__':
    pass
