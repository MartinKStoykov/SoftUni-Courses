n1 = int(input())
n2 = int(input())
operator_symbol = str(input())
n_final = 0
n_quality = ""

if operator_symbol == "+":
    n_final = n1 + n2
    if (n1 + n2) % 2 == 0:
        n_quality = "even"
    else:
        n_quality = "odd"
    print(f"{n1} {operator_symbol} {n2} = {n_final} - {n_quality}")

elif operator_symbol == "-":
    n_final = n1 - n2
    if (n1 - n2) % 2 == 0:
        n_quality = "even"
    else:
        n_quality = "odd"
    print(f"{n1} {operator_symbol} {n2} = {n_final} - {n_quality}")

elif operator_symbol == "*":
    n_final = n1 * n2
    if (n1 * n2) % 2 == 0:
        n_quality = "even"
    else:
        n_quality = "odd"
    print(f"{n1} {operator_symbol} {n2} = {n_final} - {n_quality}")

elif operator_symbol == "/":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        n_final = n1 / n2
        print(f"{n1} {operator_symbol} {n2} = {n_final:.2f}")
elif operator_symbol == "%":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        n_final = n1 % n2
        print(f"{n1} {operator_symbol} {n2} = {n_final}")
