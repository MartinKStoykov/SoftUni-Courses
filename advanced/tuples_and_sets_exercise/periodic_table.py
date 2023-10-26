chemical_count = int(input())
unique_chemicals = set()
for num in range(chemical_count):
    compound = input().split()
    unique_chemicals.update(compound)

print("\n".join(unique_chemicals))