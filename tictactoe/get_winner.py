class GetWinner():
    def get_winner(board):
        winner = False

        if board[1][1] == "O":
            if board[0][0] == "O":
                if board[2][2] == "O":
                    winner = True
                    return winner
            elif board[2][0] == "O":
                if board[0][2] == "O":
                    winner = True
                    return winner
            elif board[1][0] == "O":
                if board[1][2] == "O":
                    winner = True
                    return winner
            elif board[0][1] == "O":
                if board[2][1] == "O":
                    winner = True
                    return winner
        if board[0][0] == "O":
            if board[1][0] == "O":
                if board[2][0] =="O":
                    winner = True
                    return winner
            elif board[0][1] == "O":
                if board[0][2] == "O":
                    winner = True
                    return winner
        if board[2][2] == "O":
            if board[2][1] == "O":
                if board[2][0] == "O":
                    winner = True
                    return winner
            elif board[1][2] == "O":
                if board[0][2] == "O":
                    winner = True
                    return winner

        if board[1][1] == "X":
            if board[0][0] == "X":
                if board[2][2] == "X":
                    winner = True
                    return winner
            elif board[2][0] == "X":
                if board[0][2] == "X":
                    winner = True
                    return winner
            elif board[1][0] == "X":
                if board[1][2] == "X":
                    winner = True
                    return winner
            elif board[0][1] == "X":
                if board[2][1] == "X":
                    winner = True
                    return winner
        if board[0][0] == "X":
            if board[1][0] == "X":
                if board[2][0] =="X":
                    winner = True
                    return winner
            elif board[0][1] == "X":
                if board[0][2] == "X":
                    winner = True
                    return winner
        if board[2][2] == "X":
            if board[2][1] == "X":
                if board[2][0] == "X":
                    winner = True
                    return winner
            elif board[1][2] == "X":
                if board[0][2] == "X":
                    winner = True
                    return winner

        return winner
