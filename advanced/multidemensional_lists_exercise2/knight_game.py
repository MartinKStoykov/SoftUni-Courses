board_size = int(input())
board = []
knights = []
for i in range(board_size):
    board.append([x for x in input()])
    for j in range(board_size):
        if board[i][j] == "K":
            knights.append([i, j])
removed = 0
possible_moves = [[1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1], [-1, 2]]
while True:
    max_attacks = 0
    max_knight = []
    for knight_i, knight_j in knights:
        curr_hits = 0
        for move in possible_moves:
            move_row = knight_i + move[0]
            move_col = knight_j + move[1]
            if 0 <= move_row < board_size and 0 <= move_col < board_size and board[move_row][move_col] == "K":
                curr_hits += 1
        if curr_hits > max_attacks:
            max_attacks = curr_hits
            max_knight = [knight_i, knight_j]
    if max_attacks == 0:
        break
    board[max_knight[0]][max_knight[1]] = "0"
    knights.remove(max_knight)
    removed += 1
print(removed)




