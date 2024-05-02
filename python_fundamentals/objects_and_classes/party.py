class Party:
    def __init__(self):
        self.people = []


party = Party()
entry = input()

while entry != "End":
    party.people.append(entry)
    entry = input()

print(f'Going: {", ".join(party.people)}')
print(f'Total: {len(party.people)}')
