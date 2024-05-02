from collections import deque

food_portions = [int(x) for x in input().split(", ")]
stamina = deque([int(x) for x in input().split(", ")])

peaks_data = deque([
    ("Vihren", 80),
    ("Kutelo", 90),
    ("Banski Suhodol", 100),
    ("Polezhan", 60),
    ("Kamenitza", 70),
])

conquered_peaks = []
day = 1

while True:

    if len(conquered_peaks) == 5:
        print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
        break
    if day > 7 or not food_portions or not stamina:
        print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
        break

    current_energy = food_portions.pop() + stamina.popleft()
    current_peak_data = peaks_data.popleft()

    if current_energy >= current_peak_data[1]:
        conquered_peaks.append(current_peak_data[0])
    else:
        peaks_data.appendleft(current_peak_data)

    day += 1

if conquered_peaks:
    print("Conquered peaks: ")
    print("\n".join(conquered_peaks))
