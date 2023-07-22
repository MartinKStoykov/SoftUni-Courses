first_string = str(input())
second_string = str(input())

while first_string in second_string:
    second_string = second_string.replace(first_string, "")

print(second_string)