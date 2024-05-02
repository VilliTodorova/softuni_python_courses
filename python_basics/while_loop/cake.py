cake_length = int(input())
cake_width = int(input())

pieces_taken = 0

cake_total_pieces = cake_length * cake_width

command = input()
while command != "STOP":
    pieces_taken += int(command)
    if pieces_taken >= cake_total_pieces or command == "STOP":
        break
    command = input()

pieces_left = cake_total_pieces - pieces_taken

if pieces_left > 0 and command == "STOP":
    print(f"{pieces_left} pieces are left.")
elif pieces_left < 0:
    print(f"No more cake left! You need {abs(pieces_left)} pieces more.")
