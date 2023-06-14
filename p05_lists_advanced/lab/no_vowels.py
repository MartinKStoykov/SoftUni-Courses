vowels = ["a", "o", "u", "e", "i"]
string = str(input())
final_string = [char for char in string if char.lower() not in vowels]
print("".join(final_string))