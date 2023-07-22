tickets = input().split(", ")
for ticket in tickets:
    ticket = ticket.replace(" ", "")
    first_half = ticket[:10]
    second_half = ticket[10:]
    if len(ticket) == 20:
        length = ""
        symbol = ""
        if len(set(first_half)) == 1 and first_half == second_half:
            if "@" * 10 in first_half and "@" * 10 in second_half:
                print(f'ticket "{ticket}" - 10@ Jackpot!')
            elif  "#" * 10 in first_half and "#" * 10 in second_half:
                print(f'ticket "{ticket}" - 10# Jackpot!')
            elif  "$" * 10 in first_half and "$" * 10 in second_half:
                print(f'ticket "{ticket}" - 10$ Jackpot!')
            elif  "^" * 10 in first_half and "^" * 10 in second_half:
                print(f'ticket "{ticket}" - 10^ Jackpot!')
            else:
                print(f'ticket "{ticket}" - no match')
        elif len(set(first_half)) <= 5 and len(set(second_half)) <= 5:
            for num in range(10, 5, -1):
                if "@" * num in first_half and "@" * num in second_half:
                    print(f'ticket "{ticket}" - {num}@')
                    break
                elif "#" * num in first_half and "#" * num in second_half:
                    print(f'ticket "{ticket}" - {num}#')
                    break
                elif "$" * num in first_half and "$" * num in second_half:
                    print(f'ticket "{ticket}" - {num}$')
                    break
                elif "^" * num in first_half and "^" * num in second_half:
                    print(f'ticket "{ticket}" - {num}^')
                    break
            else:
                print(f'ticket "{ticket}" - no match')
        else:
            print(f'ticket "{ticket}" - no match')
    else:
        print("invalid ticket")