strings = input().split()
final_string = [string * len(string) for string in strings]
print("".join(final_string))