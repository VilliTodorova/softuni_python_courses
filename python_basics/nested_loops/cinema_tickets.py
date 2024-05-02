total_sold = 0
standard_sold = 0
student_sold = 0
kid_sold = 0

command = input()

while command != "Finish":
    film_name = command
    available_seats = int(input())
    seats_left = available_seats

    while seats_left > 0:
        ticket_type = input()
        purchased_tickets = 0

        if ticket_type == "End":
            break

        purchased_tickets += 1
        seats_left -= 1

        if ticket_type == "standard":
            standard_sold += 1
        elif ticket_type == "student":
            student_sold += 1
        elif ticket_type == "kid":
            kid_sold += 1

    purchased_tickets = available_seats - seats_left
    total_sold += purchased_tickets

    full_percentage = purchased_tickets / available_seats * 100
    print(f"{film_name} - {full_percentage :.2f}% full.")

    command = input()

standard_percentage = standard_sold / total_sold * 100
student_percentage = student_sold / total_sold * 100
kid_percentage = kid_sold / total_sold * 100

print(f"Total tickets: {total_sold}\n"
      f"{student_percentage :.2f}% student tickets.\n"
      f"{standard_percentage :.2f}% standard tickets.\n"
      f"{kid_percentage :.2f}% kids tickets.")
