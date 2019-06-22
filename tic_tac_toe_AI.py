import tictactoe

if '__main__' == __name__:
    turn = 0
    winner = False
    board_is_full = False
    board = tictactoe.Board.new_board()

    while winner == False and board_is_full != True:
        tictactoe.Render.print_render(board)
        move_x, move_y = tictactoe.GetMove.get_move()
        current_player = tictactoe.SwitchPlayer.switch_player(turn)
        tictactoe.MakeMove.make_move(board, move_x, move_y, current_player)
        turn += 1
        winner = tictactoe.GetWinner.get_winner(board)
        board_is_full = tictactoe.IsBoardFull.is_board_full(board)
        print(board_is_full)
    #final render, before showing result    
    tictactoe.Render.print_render(board)

    if board_is_full == True:
        print("Draw!")
    if winner == True:
        print("Winner!")
