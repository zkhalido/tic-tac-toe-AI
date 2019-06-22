move_x = 0
move_y = 0
class GetMove():

    def get_move():
        while True:
            try:
                move_x = int(input("Enter x coordinate: "))
                if move_x < 0 or move_x > 2:
                    raise ValueError
                break
            except ValueError:
                print("Invalid entry. The coordinate entered must be in the range of 0-2.")
        while True:
            try:
                move_y = int(input("Enter y coordinate: "))
                if move_y < 0 or move_y > 2:
                    raise ValueError
                break
            except ValueError:
                print("Invalid entry. The coordinate entered must be in the range of 0-2.")

        return move_x, move_y
