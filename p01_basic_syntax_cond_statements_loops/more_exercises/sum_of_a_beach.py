string = str(input())
message = string.casefold()
num = 0
num += message.count("sand") + message.count("fish") + message.count("sun") + message.count("water")
print(num)