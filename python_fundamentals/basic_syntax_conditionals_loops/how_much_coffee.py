event = input()
coffees = 0
while event != "END":
    if event.lower() == "cat" or event.lower() == "dog" or event.lower() == "coding" or event.lower() == "movie":
        if event.islower():
            coffees += 1
        else:
            coffees += 2

    event = input()

if coffees > 5:
    print("You need extra sleep")
else:
    print(coffees)

