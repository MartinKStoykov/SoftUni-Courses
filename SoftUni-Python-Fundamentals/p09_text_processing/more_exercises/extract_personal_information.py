string_count = int(input())
for count in range(string_count):
    string = str(input())
    index1 = string.index("@")+1
    index2 = string.index("|")
    name = string[index1:index2]
    index3 = string.index("#")+1
    index4 = string.index("*")
    age = string[index3:index4]
    print(f"{name} is {age} years old.")