bowl_length = float(input())
bowl_width = float(input())
bowl_height = float(input())
percent = float(input())

bowl_size = bowl_length * bowl_width * bowl_height
bowl_litres = bowl_size * 0.001

percent_of_bowl = bowl_litres - (bowl_litres *(percent / 100))

print(percent_of_bowl)

