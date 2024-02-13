numbers = input().split(", ")
positives = [number for number in numbers if int(number) >= 0]
negatives = [number for number in numbers if int(number) < 0]
even = [number for number in numbers if int(number) % 2 == 0]
odd = [number for number in numbers if int(number) % 2 == 1]
print("Positive:", ", ".join(positives))
print("Negative:", ", ".join(negatives))
print("Even:", ", ".join(even))
print("Odd:", ", ".join(odd))