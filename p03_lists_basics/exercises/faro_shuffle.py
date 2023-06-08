card_list = input().split(" ")
new_list = []
shuffle_count = int(input())
size = int(len(card_list) / 2)

for shuffle in range(shuffle_count):
    first_half = card_list[:size]
    second_half = card_list[size:]
    new_list.clear()
    for char in range(size):
        new_list.append(first_half[char])
        new_list.append(second_half[char])
    card_list = new_list
print(card_list)