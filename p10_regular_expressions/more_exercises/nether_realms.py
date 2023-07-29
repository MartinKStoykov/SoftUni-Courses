import re

text = input()
demons = re.split(r",\s*", text)
demons_stats = {}
for demon in sorted(demons):
    demon = demon.strip()
    ascii_health = re.findall(r"[^\d\-*/.+]+?", demon)
    health_sum = sum(ord(char) for char in ascii_health)

    damage_numbers = re.findall(r"-?\d+\.?\d*", demon)
    damage_sum = sum([float(num) for num in damage_numbers])
    operators = re.findall(f"[/*]", demon)


    for char in operators:
        if char == "*":
            damage_sum *= 2
        elif char == "/":
            damage_sum /= 2

    print(f"{demon} - {health_sum} health, {damage_sum:.2f} damage")


