import tictactoe

if '__main__' == __name__:
    turn = 0
    board = tictactoe.Board.new_board()
    tictactoe.Render.print_render(board)
    move_x, move_y = tictactoe.GetMove.get_move()
    current_player = tictactoe.SwitchPlayer.switch_player(turn)
    tictactoe.MakeMove.make_move(board, move_x, move_y, current_player)
    turn += 1
    tictactoe.Render.print_render(board)
    move_x, move_y = tictactoe.GetMove.get_move()
    current_player = tictactoe.SwitchPlayer.switch_player(turn)
    tictactoe.MakeMove.make_move(board, move_x, move_y, current_player)
    turn += 1
    tictactoe.Render.print_render(board)
