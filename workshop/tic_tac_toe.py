from math import ceil


def setup():
    global player_one, player_two
    player_one_name = input("Player one, please chose a name: ")
    player_two_name = input("Player two, please chose a name: ")
    player_one_sign = choose_sign(player_one_name)
    player_two_sign = "X" if player_one_sign == "0" else "0"
    player_one = [player_one_name, player_one_sign]
    player_two = [player_two_name, player_two_sign]
    print("This is the numeration of the board: ")
    print("|  1  |  2  |  3  |")
    print("|  4  |  5  |  6  |")
    print("|  7  |  8  |  9  |")
    print(f"{player_one_name} plays first!")


def choose_sign(player):
    sign = input(f"{player} would you like to use 'X' or '0'? ")
    if sign != "X" and sign != "0":
        print("Invalid sign.")
        choose_sign(player)
    return sign


def play(current, board):
    position = check_if_in_range(current)
    row = ceil(position / 3) - 1
    col = position % 3 - 1
    if check_if_space_free(row, col, board):
        board[row][col] = current[1]
        draw_board(board)
        check_if_won(current, board)
    else:
        print("Position already taken!")
        return play(current, board)


def check_if_in_range(player):
    position_num = int(input(f"{current[0]} please pick a position between 1 and 9. "))
    if not 0 < position_num < 10:
        print("Position not in range!")
        return check_if_in_range(player)
    return position_num


def check_if_space_free(row, col, board):
    return board[row][col] == " "


def check_if_won(current, board):
    global loop
    first_row = all(x == current[1] for x in board[0])
    second_row = all(x == current[1] for x in board[1])
    third_row = all(x == current[1] for x in board[2])
    first_col = all(x == current[1] for x in [board[0][0], board[1][0], board[2][0]])
    second_col = all(x == current[1] for x in [board[0][1], board[1][1], board[2][1]])
    third_col = all(x == current[1] for x in [board[0][2], board[1][2], board[2][2]])
    first_diagonal = all(x == current[1] for x in [board[0][0], board[1][1], board[2][2]])
    second_diagonal = all(x == current[1] for x in [board[0][2], board[1][1], board[2][0]])
    if any([first_row, second_row, third_row, first_col, second_col, third_col, first_diagonal, second_diagonal]):
        print(f"{current[0]} has won this game of Tic-Tac-Toe!")
        loop = False


def draw_board(board):
    for i in board:
        print("|", end="")
        print(*[f" {char}  |" for char in i])


player_one = None
player_two = None
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]
setup()
current = player_one
other = player_two
loop = True

while loop:
    play(current, board)
    current, other = other, current

