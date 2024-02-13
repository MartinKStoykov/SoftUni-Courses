import math

name_of_show = input()
length_show = int(input())
length_break = int(input())

time_to_eat = length_break * 0.125
leisure_time = length_break * 0.25

free_time = (length_break - leisure_time - time_to_eat)
if length_show <= free_time:
    leftover_time = int(math.ceil(free_time - length_show))
    print(f'You have enough time to watch {name_of_show} and left with {leftover_time} minutes free time.')
elif length_show > free_time:
    time_deficit = int(math.ceil(abs(free_time - length_show)))
    print(f"You don't have enough time to watch {name_of_show}, you need {time_deficit} more minutes.")