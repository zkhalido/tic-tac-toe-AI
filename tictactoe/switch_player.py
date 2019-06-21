class SwitchPlayer():
    def switch_player(turn):
        current_player = "X" if turn % 2 == 0 else "O"
        return current_player
