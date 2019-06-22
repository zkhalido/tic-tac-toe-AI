class MakeMove():
    def make_move(board, move_x, move_y, player):
        board[int(move_x)][int(move_y)] = player
        return board
