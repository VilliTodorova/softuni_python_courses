messages_count = int(input())

for i in range(messages_count):
    command = int(input())
    if command == 88:
        print("Hello")
    elif command == 86:
        print("How are you?")
    elif command < 88:
        print("GREAT!")
    else:
        print("Bye.")