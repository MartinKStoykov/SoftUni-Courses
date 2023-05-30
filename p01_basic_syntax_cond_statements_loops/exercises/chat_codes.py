number = int(input())
for num in range(number):
    numbers = int(input())
    if numbers == 88:
        print("Hello")
    elif numbers == 86:
        print("How are you?")
    elif numbers != 86 and numbers < 88:
        print("GREAT!")
    elif numbers > 88:
        print("Bye.")