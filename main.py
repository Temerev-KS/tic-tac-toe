from game_engine import GameEngine


def play_tic_tac_toe():
    engine = GameEngine()
    engine.clear_terminal()  # Clears everything from the console
    engine.display_logo()  # Decorative logo at the top
    engine.name_players()  # Ask users to enter their names
    engine.game_loop()  # Run the main loop responsible for the game


if __name__ == '__main__':
    play_tic_tac_toe()
