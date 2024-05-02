groups_count = int(input())
mount = ""
people_musala = 0
people_mont_blanc = 0
people_kilimanjaro = 0
people_k_2 = 0
people_everest = 0
total_people = 0

for groups in range(groups_count):
    group_size = int(input())

    if group_size <= 5:
        mount = "Musala"
        people_musala += group_size
    elif group_size <= 12:
        mount = "Mont blanc"
        people_mont_blanc += group_size
    elif group_size <= 25:
        mount = "Kilimanjaro"
        people_kilimanjaro += group_size
    elif group_size <= 40:
        mount = "K2"
        people_k_2 += group_size
    else:
        mount = "Everest"
        people_everest += group_size

    total_people += group_size

musala_percentage = people_musala / total_people * 100
mont_blanc_percentage = people_mont_blanc / total_people * 100
kilimanjaro_percentage = people_kilimanjaro / total_people * 100
k_2_percentage = people_k_2 / total_people * 100
everest_percentage = people_everest / total_people * 100

print(f"{musala_percentage:.2f}%\n"
      f"{mont_blanc_percentage:.2f}%\n"
      f"{kilimanjaro_percentage:.2f}%\n"
      f"{k_2_percentage:.2f}%\n"
      f"{everest_percentage:.2f}%")
