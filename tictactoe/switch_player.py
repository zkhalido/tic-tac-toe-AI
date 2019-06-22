class SwitchPlayer():
    def switch_player(turn):
        current_player = "X" if turn % 2 == 0 else "O"
        return current_player

    def display_player(turn):
        current_player = "X" if turn % 2 == 0 else "O"
        print("Player " + current_player + " turn.\n")
