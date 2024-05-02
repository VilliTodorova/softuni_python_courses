from math import ceil

easter_bread_count = int(input())
max_flour = 0
max_sugar = 0
sugar_needed = 0
flour_needed = 0

for bread in range(easter_bread_count):
    sugar_used_amount = int(input())
    flour_used_amount = int(input())
    sugar_needed += sugar_used_amount
    flour_needed += flour_used_amount
    if sugar_used_amount > max_sugar:
        max_sugar = sugar_used_amount
    if flour_used_amount > max_flour:
        max_flour = flour_used_amount

sugar_packs_used = ceil(sugar_needed / 950)
flour_packs_used = ceil(flour_needed / 750)

print(f"Sugar: {sugar_packs_used}\n"
      f"Flour: {flour_packs_used}\n"
      f"Max used flour is {max_flour} grams, "
      f"max used sugar is {max_sugar} grams.")
