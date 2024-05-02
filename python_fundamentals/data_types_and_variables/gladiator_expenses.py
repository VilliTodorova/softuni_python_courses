lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
broken_shield_counter = 0
expenses = 0

for loss in range(1, lost_fights_count + 1):
    if loss % 2 == 0:
        expenses += helmet_price
    if loss % 3 == 0:
        expenses += sword_price
    if loss % 2 == 0 and loss % 3 == 0:
        expenses += shield_price
        broken_shield_counter += 1

armor_mending = (broken_shield_counter // 2) * armor_price
expenses += armor_mending
print(f"Gladiator expenses: {expenses:.2f} aureus")
