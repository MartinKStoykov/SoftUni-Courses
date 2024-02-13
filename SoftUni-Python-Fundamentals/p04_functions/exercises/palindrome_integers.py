def palindrome(num):
    if int(num) == int(reversed_number(num)):
        return True
    else:
        return False
numbers = list(map(int, input().split(", ")))

def reversed_number(number):
    string = ""
    for num in range(len(number)-1, -1, -1):
        string += f"{number[num]}"
    return string

for num in numbers:
    print(palindrome(str(num)))