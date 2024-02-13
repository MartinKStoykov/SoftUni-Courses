type_projection = str(input())
rolls = int(input())
columns = int(input())

sales_income = 0
seats = rolls * columns
if type_projection == "Premiere":
    sales_income = seats * 12.00
elif type_projection == "Normal":
    sales_income = seats * 7.50
elif type_projection == "Discount":
    sales_income = seats * 5.00
print(f"{sales_income:.2f} leva")