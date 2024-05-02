favourite_book = input()
command = input()
checked_books = 0

while command != "No More Books":
    current_book = command
    if current_book == favourite_book:
        break
    checked_books += 1
    command = input()

if command != "No More Books":
    print(f"You checked {checked_books} books and found it.")
else:
    print(f"The book you search is not here!\nYou checked {checked_books} books.")
