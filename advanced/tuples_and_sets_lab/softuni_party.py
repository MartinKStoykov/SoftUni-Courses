guest_number = int(input())
reservation_list = set()
for guest in range(guest_number):
    reservation_list.add(input())

check_in = input()
while check_in != "END":
    if check_in in reservation_list:
        reservation_list.remove(check_in)
    check_in = input()
sorted_reservations = sorted(reservation_list, key=lambda x: x[0])
print(len(sorted_reservations))
print("\n".join(sorted_reservations))