jury_number = int(input())
is_running = True
total_rating = 0
number_of_presentations = 0
while is_running:
    presentation_name = str(input())
    rating_per_person = 0
    if presentation_name == "Finish":
        is_running = False
        break
    for rating in range(jury_number):
        current_rating = float(input())
        rating_per_person += current_rating
    number_of_presentations += 1
    average_rating = rating_per_person / jury_number
    print(f"{presentation_name} - {average_rating:.2f}.")
    total_rating += average_rating
    average_total_rating = total_rating / number_of_presentations


print(f"Student's final assessment is {average_total_rating:.2f}.")