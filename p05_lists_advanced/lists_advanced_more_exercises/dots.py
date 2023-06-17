def find_dot(string):
    for row in range(len(string)):
        for col in range(len(string[0])):
            if string[row][col] == ".":
                return [row, col]
    return False
def neighbour_dot(string, cord):
    directions = []
    if not cord[1]-1 < 0:
        left = [cord[0], cord[1] - 1]
        directions.append(left)
    if not cord[1]+1 > len(string[0])-1:
        right = [cord[0], cord[1] + 1]
        directions.append(right)
    if not cord[0]-1 < 0:
        up = [cord[0] - 1, cord[1]]
        directions.append(up)
    if not cord[0] == len(string)-1:
        down = [cord[0] + 1,  cord[1]]
        directions.append(down)
    return directions
board_rows = int(input())
board = []
for _ in range(board_rows):
    board.append(str(input()).split(" "))
dots_list = [0]
dots = 0

coordinate_list = []
while find_dot(board):
    current_location = find_dot(board)
    locations = []
    dots_counted = False
    while not dots_counted:
        locations = neighbour_dot(board, [current_location[0], current_location[1]])
        if board[current_location[0]][current_location[1]] == ".":
            board[current_location[0]][current_location[1]] = "v"
            dots += 1
            coordinate_list.append([current_location[0], current_location[1]])
        for coordinate in coordinate_list:
            found = 0
            locations = neighbour_dot(board, [coordinate[0], coordinate[1]])
            for cord in locations:
                if board[cord[0]][cord[1]] == ".":
                    board[cord[0]][cord[1]] = "v"
                    current_location = [cord[0],cord[1]]
                    dots += 1
                    found += 1
                    coordinate_list.append([cord[0], cord[1]])
        dots_list.append(dots)
        dots = 0
        current_location = find_dot(board)
        dots_counted = True
print(max(dots_list))