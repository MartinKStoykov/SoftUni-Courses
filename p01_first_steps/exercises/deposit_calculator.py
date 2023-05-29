deposited_sum = float(input())
months = int(input())
interest_rate = float(input())

yearly_interest_rate = deposited_sum * (interest_rate / 100)
monthly_rate = yearly_interest_rate / 12
total_sum = deposited_sum + months * monthly_rate
print(total_sum)


