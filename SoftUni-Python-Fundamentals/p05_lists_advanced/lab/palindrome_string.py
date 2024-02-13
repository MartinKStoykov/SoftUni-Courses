string = input().split()
palindrome = str(input())
palindromes = [word for word in string if word == word[::-1]]
instances = [word for word in string if word == palindrome]
print(palindromes)
print(f"Found palindrome {len(instances)} times")