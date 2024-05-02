open_tabs = int(input())
salary = int(input())
fine = 0
for _ in range(open_tabs):
    current_tab = input()

    if current_tab == "Facebook":
        fine += 150
    elif current_tab == "Instagram":
        fine += 100
    elif current_tab == "Reddit":
        fine += 50
    else:
        pass
    if fine >= salary:
        break

leftover = salary - fine

if leftover > 0:
    print(f"{int(leftover)}")
else:
    print("You have lost your salary.")

