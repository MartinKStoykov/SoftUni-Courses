import re

regex = r"www\.[A-Za-z0-9\-]+[\.a-z]*\.[a-z]+"
while True:
    text = input()
    if not text:
        break
    found_site = re.findall(regex, text)
    if found_site:
        print(*found_site)