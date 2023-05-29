budget = float(input())
number_of_gpu = int(input())
number_of_cpu = int(input())
number_of_ram = int(input())

total_gpu_price = number_of_gpu * 250
total_cpu_price = (total_gpu_price * 0.35) * number_of_cpu
total_ram_price = (total_gpu_price * 0.10) * number_of_ram

final_price = total_ram_price + total_gpu_price + total_cpu_price

if number_of_gpu > number_of_cpu:
    final_price *= 0.85
if budget >= final_price:
    budget -= final_price
    print(f"You have {budget:.2f} leva left!")
elif budget < final_price:
    budget = abs(budget - final_price)
    print(f"Not enough money! You need {budget:.2f} leva more!")


