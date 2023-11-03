n = int(input())
intersections = []
for num in range(n):
    first_range, second_range = input().split("-")
    n1, n2 = first_range.split(",")
    m1, m2 = second_range.split(",")
    first_length = set(int(num) for num in range(int(n1), int(n2)+1))
    second_length = set(int(num) for num in range(int(m1), int(m2)+1))
    if len(list(first_length.intersection(second_length))) > len(intersections):
        intersections = list(first_length.intersection(second_length))

print(f"Longest intersection is {intersections} with length {len(intersections)}")