def check_forwards(board, player, curr_cords, next_direction, dots):
    try:
        if dots < 4 and board[curr_cords[0] + next_direction[0]][curr_cords[1] + next_direction[1]] == player:
            dots += 1
            return check_forwards(board, player, [curr_cords[0] + next_direction[0], curr_cords[1] + next_direction[1]],
                                  next_direction, dots)
        return dots
    except IndexError:
        return dots


def check_backwards(board, player, curr_cords, next_direction, dots):
    try:
        if dots < 4 and board[curr_cords[0] - next_direction[0]][curr_cords[1] - next_direction[1]] == player:
            dots += 1
            return check_backwards(board, player, [curr_cords[0] - next_direction[0],
                                                   curr_cords[1] - next_direction[1]], next_direction, dots)
        return dots
    except IndexError:
        return dots


def check_if_winner(board, player, cord):
    directions = [[0, 1], [1, 0], [1, 1], [-1, 1]]
    for r, c in directions:
        if check_forwards(board, player, cord, [r, c], 1) + check_backwards(board, player, cord, [r, c], 0) == 4:
            return True
    return False


def check_if_valid(board, player, col):
    try:
        if 0 <= int(col) <= 7:
            return place_slot(board, player, int(col) - 1)

        else:
            return check_if_valid(board, player, input(f"Number not in range. "
                                                       f"Player {player}, please pick a column between 1 and 7: "))
    except ValueError:
        return check_if_valid(board, player,
                              input(f"Number needed. Player {player}, please pick a column between 1 and 7: "))


def place_slot(board, player, col):
    for row in range(5, -1, -1):
        if board[row][col] == 0:
            board[row][col] = player
            return check_if_winner(board, player, [row, col])

    return check_if_valid(board, player, int(input(f"No more space in column {col}. "
                                                   f"Player {player}, please pick another column: ")))


def print_board(board):
    return [print(row) for row in board]


game_board = [[0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0]
              ]
player_num = 0
while True:
    current_player = 1 if player_num % 2 == 0 else 2
    if check_if_valid(game_board, current_player,
                      input(f"Player {current_player}, please pick a column between 1 and 6: ")):
        print(f"Congratulations Player {current_player}! You have won this game of connect four!")
        print_board(game_board)
        break
    print_board(game_board)

    player_num += 1
