number = int(input())
operation = True
count = 0
password = ""
password_found = False
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if (a < b and c > d) and a * b + c * d == number:
                    count += 1
                    if count == 4:
                        password_found = True
                        password = f"{a}{b}{c}{d}"
                    print(f"{a}{b}{c}{d}", end=" ")
print()
if password:
    print(f"Password: {password}")
else:
    print(f"No!")
