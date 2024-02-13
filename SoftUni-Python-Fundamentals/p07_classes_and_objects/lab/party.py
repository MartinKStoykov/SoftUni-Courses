class Party:
    def __init__(self):
        self.people = []

party = Party()
command = str(input())
while command != "End":
    party.people.append(command)
    command = str(input())

print("Going:", ", ".join(party.people))
print("Total:", len(party.people))