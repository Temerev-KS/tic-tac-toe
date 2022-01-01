from game_engine import GameEngine


def func():
    pass


if __name__ == '__main__':
    engine = GameEngine()
    engine.clear_terminal()
    engine.show_logo()
    engine.name_players()
    engine._players[0]._victories = 2
    while engine.is_game_on():
        while not engine.check_for_winner():
            while not engine.check_winning_combo_present():
                if engine.board_has_empty_cells():
                    engine.change_player()
                    # engine._players[0]._victories = 2
                    engine.move()
                else:
                    engine.result_draw()
            # engine._board.empty()
        engine.repeat_game_input()
    print('Good by!')
        
        

    
