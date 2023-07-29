import re

message_number = int(input())
attacked_planets = []
destroyed_planets = []
for num in range(message_number):
    message = input()
    letter_count = len(re.findall(r"[star]", message, re.I))
    decrypted_message = ""
    for char in message:
        decrypted_message += chr(ord(char) - letter_count)

    regex = r"@([A-Za-z]+)[^@!:>]*?:(\d+)[^@!:>]*?!([AD])![^@!:>]*?->.*?(\d+).*?"
    planet_found = re.findall(regex, decrypted_message)
    if planet_found:
        if planet_found[0][2] == "A":
            attacked_planets.append(planet_found[0][0])
        else:
            destroyed_planets.append(planet_found[0][0])

print(f"Attacked planets: {len(attacked_planets)}")
if attacked_planets:
    for planet in sorted(attacked_planets):
        print(f"-> {planet}")
print(f"Destroyed planets: {len(destroyed_planets)}")
if destroyed_planets:
    for planet in sorted(destroyed_planets):
        print(f"-> {planet}")