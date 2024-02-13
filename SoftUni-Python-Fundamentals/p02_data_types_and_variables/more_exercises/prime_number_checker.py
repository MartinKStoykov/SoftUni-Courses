number = int(input())
for num in range(2, number):
    if number % num == 0:
        print(f"False")
        break
else:
    print(f"True")