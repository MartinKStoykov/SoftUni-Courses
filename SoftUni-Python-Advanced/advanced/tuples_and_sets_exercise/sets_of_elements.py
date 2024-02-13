n, m = input().split()
n_set = set()
m_set = set()
for num1 in range(int(n)):
    n_set.add(input())

for num2 in range(int(m)):
    m_set.add(input())

common_elements = n_set.intersection(m_set)
print("\n".join(common_elements))
