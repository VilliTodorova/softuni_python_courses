flavour = input()   # "Watermelon", "Mango", "Pineapple" OR "Raspberry"
package_type = input()  # "small" x 2 OR "big" x 5
ordered_packages = int(input())
price_per_pack = 0

if flavour == "Watermelon":
    if package_type == "small":
        price_per_pack = 56 * 2
    elif package_type == "big":
        price_per_pack = 28.70 * 5
elif flavour == "Mango":
    if package_type == "small":
        price_per_pack = 36.66 * 2
    elif package_type == "big":
        price_per_pack = 19.60 * 5
elif flavour == "Pineapple":
    if package_type == "small":
        price_per_pack = 42.10 * 2
    elif package_type == "big":
        price_per_pack = 24.80 * 5
elif flavour == "Raspberry":
    if package_type == "small":
        price_per_pack = 20 * 2
    elif package_type == "big":
        price_per_pack = 15.20 * 5

total_price = ordered_packages * price_per_pack
if 400 <= total_price <= 1000:
    total_price *= 0.85
elif total_price > 1000:
    total_price *= 0.5

print(f"{total_price :.2f} lv.")
