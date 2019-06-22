class MakeMove():
    def make_move(board, move_x, move_y, player):
        board[int(move_y)][int(move_x)] = player
        return board
