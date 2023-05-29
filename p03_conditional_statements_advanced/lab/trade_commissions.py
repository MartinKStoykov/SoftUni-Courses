city = str(input())
sale_quantity = float(input())
commission = 0
if city == "Sofia" and not sale_quantity < 0:
    if 0 <= sale_quantity <= 500:
        commission = sale_quantity * 0.05
    elif 500 < sale_quantity <= 1000:
        commission = sale_quantity * 0.07
    elif 1000 < sale_quantity <= 10000:
        commission = sale_quantity * 0.08
    elif 10000 < sale_quantity:
        commission = sale_quantity * 0.12
    print(f"{commission:.2f}")
elif city == "Varna" and not sale_quantity < 0:
    if 0 <= sale_quantity <= 500:
        commission = sale_quantity * 0.045
    elif 500 < sale_quantity <= 1000:
        commission = sale_quantity * 0.075
    elif 1000 < sale_quantity <= 10000:
        commission = sale_quantity * 0.10
    elif 10000 < sale_quantity:
        commission = sale_quantity * 0.13
    print(f"{commission:.2f}")
elif city == "Plovdiv" and not sale_quantity < 0:
    if 0 <= sale_quantity <= 500:
        commission = sale_quantity * 0.055
    elif 500 < sale_quantity <= 1000:
        commission = sale_quantity * 0.08
    elif 1000 < sale_quantity <= 10000:
        commission = sale_quantity * 0.12
    elif 10000 < sale_quantity:
        commission = sale_quantity * 0.145
    print(f"{commission:.2f}")
else:
    print("error")