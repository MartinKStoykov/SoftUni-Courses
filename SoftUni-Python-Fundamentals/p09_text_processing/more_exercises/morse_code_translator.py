sentence = input().split("|")
final_message = ""
morse_code = {".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E", "..-.": "F", "--.": "G", "....": "H",
                "..": "I", ".---": "J", "-.-": "K", ".-..": "L", "--": "M", "-.": "N", "---": "O", ".--.":
                "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T", "..-": "U", "...-": "V", ".--": "W",
                "-..-": "X", "-.--": "Y", "--..": "Z"}
current_sentence = ""
for word in sentence:
    letters = word.split()

    for letter in letters:
        current_sentence += morse_code[letter]
    current_sentence += " "

print(current_sentence)