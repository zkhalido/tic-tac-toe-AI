import tictactoe

if '__main__' == __name__:
    turn = 0
    board = Board.new_board()
    render.Render.print_render(board)
    move_x, move_y = get_move.GetMove.get_move()
    current_player = switch_player.SwitchPlayer.switch_player(turn)
    make_move.MakeMove.make_move(board, move_x, move_y, current_player)
    turn += 1
    render.Render.print_render(board)
    move_x, move_y = get_move.GetMove.get_move()
    current_player = switch_player.SwitchPlayer.switch_player(turn)
    make_move.MakeMove.make_move(board, move_x, move_y, current_player)
    render.Render.print_render(board)
