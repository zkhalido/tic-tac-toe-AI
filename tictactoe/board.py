board_latitude = 3
board_longitude = 3

class Board(object):
    def new_board():
        toe_board = [[" " for i in range(board_latitude)] for j in range(board_longitude)]
        return toe_board
