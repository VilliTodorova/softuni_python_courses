commands_count = int(input())
parked_vehicles = {}

for _ in range(commands_count):
    command = input().split()
    username = command[1]

    if command[0] == 'register':    # register {username} {license_plate_number}
        license_plate_number = command[2]
        if username in parked_vehicles:
            print(f'ERROR: already registered with plate number {license_plate_number}')
        else:
            parked_vehicles[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")
    elif command[0] == 'unregister':    # unregister {username}
        if username not in parked_vehicles:
            print(f"ERROR: user {username} not found")
        else:
            del parked_vehicles[username]
            print(f"{username} unregistered successfully")

for (key, value) in parked_vehicles.items():
    print(f"{key} => {value}")
