decorations_quantity = int(input())  # to buy each time you go shopping
days_left = int(input())  # until Christmas
ornament_set_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights_price = 15

total_cost = 0
total_spirit = 0

for current_day in range(1, days_left + 1):
    if current_day % 11 == 0:
        decorations_quantity += 2
    if current_day % 2 == 0:
        total_spirit += 5
        total_cost += decorations_quantity * ornament_set_price
    if current_day % 3 == 0:
        total_spirit += 10 + 3
        total_cost += decorations_quantity * (tree_skirt_price + tree_garland_price)
    if current_day % 5 == 0:
        total_spirit += 17
        total_cost += decorations_quantity * tree_lights_price
        if current_day % 3 == 0:
            total_spirit += 30
    if current_day % 10 == 0:
        total_spirit -= 20
        total_cost += (tree_skirt_price + tree_garland_price + tree_lights_price)

if days_left % 10 == 0:
    total_spirit -= 30

print(f"Total cost: {total_cost}\n"
      f"Total spirit: {total_spirit}")
