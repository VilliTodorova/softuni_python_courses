def flights(*flights_data):
    flight_dict = {}
    i = 0

    while flights_data[i] != "Finish":
        destination = flights_data[i]
        passengers = flights_data[i + 1]
        if destination in flight_dict:
            flight_dict[destination] += passengers
        else:
            flight_dict[destination] = passengers

        i += 2

    return flight_dict


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))