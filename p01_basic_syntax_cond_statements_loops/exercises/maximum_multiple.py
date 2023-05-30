from sys import maxsize
divisor = int(input())
boundary = int(input())
biggest_number = 0
for num in range(1, boundary+1,):
    if num > 0 and num % divisor == 0:
        biggest_number = num
print(biggest_number)
