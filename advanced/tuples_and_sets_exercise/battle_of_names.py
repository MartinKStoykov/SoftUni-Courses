n = int(input())
even_numbers = set()
odd_numbers = set()

for num in range(1, n+1):
    name = input()
    ascii_sum = sum(ord(char) for char in name)
    ascii_value = ascii_sum // num
    if ascii_value % 2 == 0:
        even_numbers.add(ascii_value)

    else:
        odd_numbers.add(ascii_value)


if sum(even_numbers) == sum(odd_numbers):
    print(", ".join(map(str, even_numbers.union(odd_numbers))))

elif sum(even_numbers) < sum(odd_numbers):
    print(", ".join(map(str, odd_numbers.difference(even_numbers))))

else:
    print(", ".join(map(str, even_numbers.symmetric_difference(odd_numbers))))