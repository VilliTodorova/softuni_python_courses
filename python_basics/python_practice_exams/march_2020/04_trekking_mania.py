groups_count = int(input())
total_people = 0
musala_total = 0
mont_blanc_total = 0
kilimanjaro_total = 0
k2_total = 0
everest_total = 0

for groups in range(groups_count):
    people_count = int(input())

    if people_count <= 5:
        peak_to_climb = "Musala"
        musala_people = people_count
        musala_total += musala_people
    elif people_count <= 12:
        peak_to_climb = "Mont Blanc"
        mont_blanc_people = people_count
        mont_blanc_total += mont_blanc_people
    elif people_count <= 25:
        peak_to_climb = "Kilimanjaro"
        kilimanjaro_people = people_count
        kilimanjaro_total += kilimanjaro_people
    elif people_count <= 40:
        peak_to_climb = "K2"
        k2_people = people_count
        k2_total += k2_people
    else:
        peak_to_climb = "Everest"
        everest_people = people_count
        everest_total += everest_people

    total_people += people_count

musala_percentage = musala_total / total_people * 100
mont_blanc_percentage = mont_blanc_total / total_people * 100
kilimanjaro_percentage = kilimanjaro_total / total_people * 100
k2_percentage = k2_total / total_people * 100
everest_percentage = everest_total / total_people * 100

print(f"{musala_percentage :.2f}%\n"
      f"{mont_blanc_percentage :.2f}%\n"
      f"{kilimanjaro_percentage :.2f}%\n"
      f"{k2_percentage :.2f}%\n"
      f"{everest_percentage :.2f}%")
