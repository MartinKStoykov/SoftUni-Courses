string = input().split(".")
version = list(map(int, string))
version[2] += 1
if version[2] == 10:
    version[2] = 0
    version[1] += 1
if version[1] == 10:
    version[1] = 0
    version[0] += 1
final_version = (map(str, version))
print(".".join(final_version))
