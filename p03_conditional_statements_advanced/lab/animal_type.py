animal = str(input())
mammals = ["dog"]
reptile = ["snake", "tortoise", "crocodile"]

if animal in mammals:
    print("mammal")
elif animal in reptile:
    print("reptile")
else:
    print("unknown")