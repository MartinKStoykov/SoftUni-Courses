def redistribution(people, minimum):
    if sum(people) / len(people) < minimum:
        return "No equal distribution possible"
    people_after_redistribution = []
    for person in people:
        max_num = people.index(max(people))
        if person < minimum:
            people_after_redistribution.append(minimum)
            people[max_num] = people[max_num] - (minimum - person)
        else:
            people_after_redistribution.append(person)

    return people_after_redistribution


population = list(map(int,input().split(", ")))
min_wealth = int(input())
print(redistribution(population,min_wealth))
