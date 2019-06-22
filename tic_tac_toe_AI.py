import tictactoe

if '__main__' == __name__:
    turn = 0
    winner = False
    board_is_full = False
    board = tictactoe.Board.new_board()

    while winner == False and board_is_full != True:
        tictactoe.Render.print_render(board)
        tictactoe.SwitchPlayer.display_player(turn)
        #loops till empty coordinate is entered
        while True:
            try:
                move_y, move_x = tictactoe.GetMove.get_move(board)
                if tictactoe.IsMoveValid.is_move_valid(board, move_x, move_y) == False:
                    raise ValueError
                break
            except ValueError:
                print("The position entered is taken.")

        current_player = tictactoe.SwitchPlayer.switch_player(turn)
        tictactoe.MakeMove.make_move(board, move_x, move_y, current_player)
        turn += 1
        winner = tictactoe.GetWinner.get_winner(board)
        board_is_full = tictactoe.IsBoardFull.is_board_full(board)
    #final render, before showing result
    tictactoe.Render.print_render(board)

    if board_is_full == True:
        print("Draw!")
    if winner == True:
        print("Player " + current_player + " is the winner!")
