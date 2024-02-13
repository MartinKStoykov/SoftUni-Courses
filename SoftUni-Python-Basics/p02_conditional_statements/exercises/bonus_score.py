starting_score = int(input())
bonus_score = 0

if starting_score < 100:
    bonus_score = 5
elif 100 < starting_score < 1000:
    bonus_score = starting_score * 0.20
elif starting_score > 1000:
    bonus_score = starting_score * 0.10

if starting_score % 2 == 0:
    bonus_score += 1
elif starting_score % 10 == 5:
    bonus_score += 2
total_score = starting_score + bonus_score

print(float(bonus_score))
print(float(total_score))

