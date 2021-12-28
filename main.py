from game_engine import GameEngine


def func():
    pass


if __name__ == '__main__':
    engine = GameEngine()
    engine.show_logo()
    engine.name_players()
    while engine.is_game_on():
        while engine.check_for_winner():
            while not engine.check_winning_combo_present():
                engine.change_player()
                engine.move()
            engine._board.empty()
        engine.repeat_game_input()
    print('Good by!')
        
        

    
