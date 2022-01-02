from game_engine import GameEngine


def play_tic_tac_toe():
    engine = GameEngine()
    engine.clear_terminal()
    engine.show_logo()
    engine.name_players()
    engine.game_loop()


if __name__ == '__main__':
    play_tic_tac_toe()
