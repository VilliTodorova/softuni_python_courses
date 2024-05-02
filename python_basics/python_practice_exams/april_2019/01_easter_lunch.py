easter_bread_count = int(input())
egg_packs_count = int(input())  # 12 eggs per pack  # dye = 0.15 per egg
cookies_kg = int(input())

price_easter_bread = easter_bread_count * 3.20
price_eggs = egg_packs_count * 4.35
price_cookies = cookies_kg * 5.40
price_egg_dye = egg_packs_count * 12 * 0.15

total_price = price_eggs + price_cookies + price_egg_dye + price_easter_bread

print(f"{total_price :.2f}")
