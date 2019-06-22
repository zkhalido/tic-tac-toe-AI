class IsBoardFull():
    def is_board_full(board):
        board_is_full = True
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board_is_full = False
                    break;
        return board_is_full
