matrix_size = int(input())
wonderland = []
alice = []
for i in range(matrix_size):
    wonderland.append(input().split())
    if "A" in wonderland[i]:
        alice = [i, wonderland[i].index("A")]
        wonderland[i][alice[1]] = "*"

tea_bags = 0
row = alice[0]
col = alice[1]
while True:
    action = input()

    if action == "up":
        row -= 1
    elif action == "right":
        col += 1
    elif action == "down":
        row += 1
    elif action == "left":
        col -= 1

    if not (0 <= row < matrix_size) or not (0 <= col < matrix_size):
        print("Alice didn't make it to the tea party.")
        break

    if wonderland[row][col].isdigit():
        tea_bags += int(wonderland[row][col])

    if wonderland[row][col] == "R":
        print("Alice didn't make it to the tea party.")
        wonderland[row][col] = "*"
        break

    wonderland[row][col] = "*"
    if tea_bags >= 10:
        print("She did it! She went to the party.")
        break
for x in wonderland:
    print(*x)