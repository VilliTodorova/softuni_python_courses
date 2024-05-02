flour_price_kg = float(input())
kg_flour = float(input())
kg_sugar = float(input())
eggs_pack_count = int(input())
yeast_packs = int(input())

sugar_price_kg = flour_price_kg * 0.75
eggs_pack_price = flour_price_kg * 1.1
yeast_price = sugar_price_kg * 0.2

total_price = flour_price_kg * kg_flour + \
              kg_sugar * sugar_price_kg + \
              eggs_pack_price * eggs_pack_count + \
              yeast_price * yeast_packs

print(f"{total_price :.2f}")
