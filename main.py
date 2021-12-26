from game_engine import GameEngine


def func():
    pass


if __name__ == '__main__':
    engine = GameEngine()
    engine.name_players()
    while engine.check_for_winner():
        while not engine.check_winning_combo_present():
            engine.change_player()
            engine.show_board()
            engine.move()
        

    
