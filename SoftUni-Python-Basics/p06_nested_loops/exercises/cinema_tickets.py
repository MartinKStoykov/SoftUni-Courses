command = str(input())
standard_tickets = 0
student_tickets = 0
kid_tickets = 0
taken_seats = 0
while command != "Finish":
    taken_seats_in_film = 0
    free_seats = int(input())
    for seat in range(free_seats):
        ticket_type = str(input())
        if ticket_type == "standard":
            standard_tickets += 1
        elif ticket_type == "student":
            student_tickets += 1
        elif ticket_type == "kid":
            kid_tickets += 1
        if free_seats == seat or ticket_type == "End":
            break
        taken_seats += 1
        taken_seats_in_film += 1
    if command == "Finish":
        break
    how_full = taken_seats_in_film / free_seats * 100
    print(f"{command} - {how_full:.2f}% full.")
    command = str(input())
percent_student = student_tickets / taken_seats * 100
percent_standard = standard_tickets / taken_seats * 100
percent_kid = kid_tickets / taken_seats * 100
print(f"Total tickets: {taken_seats}")
print(f"{percent_student:.2f}% student tickets.")
print(f"{percent_standard:.2f}% standard tickets.")
print(f"{percent_kid:.2f}% kids tickets.")