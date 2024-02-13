import string
last_sector = str(input())
first_sector_rows = int(input())
seats_odd = int(input())
start_sector = "A"
seats = 0
for sector in range(ord(start_sector), ord(last_sector) + 1):
    for row in range(1, first_sector_rows+1):
        if row % 2 == 0:
            for seat in range(97, (seats_odd + 97) + 2):
                print(f"{chr(sector).upper()}{row}{chr(seat)}")
                seats += 1
        else:
            for seat in range(97, (seats_odd + 97)):
                print(f"{chr(sector).upper()}{row}{chr(seat)}")
                seats += 1
    first_sector_rows += 1
print(seats)