
notes = []
while True:
    command = input().split("-")
    if command[0] == "End":
        break
    importance = int(command[0])
    note = command[1]
    notes.append((importance, note))
sorted_notes = [note[1] for note in sorted(notes)]
print(sorted_notes)
