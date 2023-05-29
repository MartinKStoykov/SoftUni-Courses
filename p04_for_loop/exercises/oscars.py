actor_name = input()
score = float(input())
number_of_scorers = int(input())

for scorer in range(number_of_scorers):
    scorer_name = input()
    individual_score = float(input())
    score += len(scorer_name) * (individual_score / 2)
    if score > 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {score:.1f}!")
        break
if score <= 1250.5:
    diff = abs(1250.5 - score)
    print(f"Sorry, {actor_name} you need {diff:.1f} more!")

