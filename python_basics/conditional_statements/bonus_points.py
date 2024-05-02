points = int(input())
# •	Ако числото е до 100 включително, бонус точките са 5;
# •	Ако числото е по-голямо от 100, бонус точките са 20% от числото;
# •	Ако числото е по-голямо от 1000, бонус точките са 10% от числото.
#
# •	Допълнителни бонус точки (начисляват се отделно от предходните):
# o	За четно число  + 1 т.
# o	За число, което завършва на 5  + 2 т.

bonus_points = 0

if points <= 100:
    bonus_points = 5
elif points <= 1000:
    bonus_points = points * 0.20
else:
    bonus_points = points * 0.10

bonus_extra = 0
if points % 2 == 0:
    bonus_extra += 1

if points % 10 == 5:
    bonus_extra += 2

print(bonus_points + bonus_extra)
print(points + bonus_points + bonus_extra)
