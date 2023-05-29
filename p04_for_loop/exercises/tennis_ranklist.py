tournament_numbers = int(input())
starting_points = int(input())
final_points = 0
percentage = 0
for num in range(tournament_numbers):
    tournament_stage = input()
    if tournament_stage == "W":
        final_points += 2000
        percentage += 1
    elif tournament_stage == "F":
        final_points += 1200
    elif tournament_stage == "SF":
        final_points += 720

average_points = final_points // tournament_numbers
percentage_won = percentage / tournament_numbers * 100
final_points += starting_points
print(f"Final points: {final_points}")
print(f"Average points: {average_points}")
print(f"{percentage_won:.2f}%")
