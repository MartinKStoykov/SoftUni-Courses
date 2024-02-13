def palindrome(word, index):
    if word[index] != word[-1-index]:
        return f"{word} is not a palindrome"
    elif len(word) == index+1:
        return f"{word} is a palindrome"
    return palindrome(word, index+1)
print(palindrome("peter", 0))