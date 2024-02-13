rows, columns = input().split()
for i in range(int(rows)):
    for j in range(int(columns)):
        print(f"{chr(97+i)}{chr(97+i+j)}{chr(97+i)}", end=" ")
    print()