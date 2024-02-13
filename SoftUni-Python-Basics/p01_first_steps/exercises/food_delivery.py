number_of_poultry = int(input())
number_of_fish = int(input())
number_of_vegan = int(input())

poultry_menu = 10.35
fish_menu = 12.40
vegan_menu = 8.15

total_poultry = number_of_poultry * poultry_menu
total_fish = number_of_fish * fish_menu
total_vegan = number_of_vegan * vegan_menu

total_menu_price = total_vegan + total_fish + total_poultry
desert_price = total_menu_price * 0.20
final_price = total_menu_price + desert_price + 2.50

print(final_price)