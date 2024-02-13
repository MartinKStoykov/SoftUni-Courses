def closed(kate, labyrinth):
    left = labyrinth[kate[0]][kate[1] - 1]
    right = labyrinth[kate[0]][kate[1] + 1]
    up = labyrinth[kate[0] - 1][kate[1]]
    down = labyrinth[kate[0] + 1][kate[1]]
    closed_spaces = 0
    if left != " ":
        closed_spaces += 1
    if right != " ":
        closed_spaces += 1
    if up != " ":
        closed_spaces += 1
    if down != " ":
        closed_spaces += 1
    return closed_spaces
def movement(kate, labyrinth):
    while True:
        crack = len(labyrinth[0])
        if kate[0] == 0 or kate[0] == len(labyrinth)-1 or kate[1] == 0 or kate[1] == len(labyrinth[0]):
            moves = 0
            for row in labyrinth:
                moves += row.count(" ")
                moves += row.count("k")
            return f"Kate got out in {moves} moves"
        if closed(kate, labyrinth) == 4:
            return "Kate cannot get out"
        directions = [[kate[0], kate[1]-1], [kate[0], kate[1]+1], [kate[0]-1, kate[1]], [kate[0]+1, kate[1]]]
        last_position = kate
        for direction in directions:
            next = [i for i in direction]
            if labyrinth[next[0]][next[1]] == " ":
                kate = next[0], next[1]
                labyrinth[next[0]][next[1]] = "k"
                break
rows = int(input())
maze = []
kate_row = 0
kate_index = 0
for row in range(rows):
    structure = [i for i in str(input())]
    if "k" in structure:
        kate_row = row
        kate_index = structure.index("k")

    maze.append(structure)
print(movement((kate_row, kate_index), maze))
