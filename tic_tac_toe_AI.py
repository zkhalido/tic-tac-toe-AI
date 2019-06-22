import tictactoe

if '__main__' == __name__:
    turn = 0
    winner = False
    board = tictactoe.Board.new_board()

    while winner == False:
        tictactoe.Render.print_render(board)
        move_x, move_y = tictactoe.GetMove.get_move()
        current_player = tictactoe.SwitchPlayer.switch_player(turn)
        tictactoe.MakeMove.make_move(board, move_x, move_y, current_player)
        turn += 1
        winner = tictactoe.GetWinner.get_winner(board)

    tictactoe.Render.print_render(board)
    if winner == True:
        print("\nWinner")
