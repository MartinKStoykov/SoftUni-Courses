clients_men = int(input())
clients_women = int(input())
max_tables = int(input())
tables = 0
operation = True
for man in range(1, clients_men+1):
    for woman in range(1, clients_women+1):
        if tables == max_tables:
            operation = False
            break
        else:
            print(f"({man} <-> {woman})", end=" ")
            tables += 1
    if not operation:
        break