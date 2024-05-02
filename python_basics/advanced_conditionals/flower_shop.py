chrysanthemum_purchased = int(input())
roses_purchased = int(input())
tulips_purchased = int(input())
season = input()
is_holiday = input()
bouquet_price = 0

flower_prices = {
    "Chrysanthemum": [2.00, 3.75],
    "Roses": [4.10, 4.50],
    "Tulips": [2.50, 4.15]
}

if is_holiday == "Y":
    for flower in flower_prices:
        flower_prices[flower][0] *= 1.15
        flower_prices[flower][1] *= 1.15

if season == "Spring":
    bouquet_price = chrysanthemum_purchased * flower_prices["Chrysanthemum"][0] + \
                    roses_purchased * flower_prices["Roses"][0] + \
                    tulips_purchased * flower_prices["Tulips"][0]
    if tulips_purchased > 7:
        bouquet_price *= 0.95
    if (chrysanthemum_purchased + roses_purchased + tulips_purchased) > 20:
        bouquet_price *= 0.80

elif season == "Summer":
    bouquet_price = chrysanthemum_purchased * flower_prices["Chrysanthemum"][0] + \
                    roses_purchased * flower_prices["Roses"][0] + \
                    tulips_purchased * flower_prices["Tulips"][0]
    if (chrysanthemum_purchased + roses_purchased + tulips_purchased) > 20:
        bouquet_price *= 0.80
elif season == "Winter":
    bouquet_price = chrysanthemum_purchased * flower_prices["Chrysanthemum"][1] + \
                    roses_purchased * flower_prices["Roses"][1] + \
                    tulips_purchased * flower_prices["Tulips"][1]
    if roses_purchased >= 10:
        bouquet_price *= 0.90
    if (chrysanthemum_purchased + roses_purchased + tulips_purchased) >= 20:
        bouquet_price *= 0.80
elif season == "Autumn":
    bouquet_price = chrysanthemum_purchased * flower_prices["Chrysanthemum"][1] + \
                    roses_purchased * flower_prices["Roses"][1] + \
                    tulips_purchased * flower_prices["Tulips"][1]
    if (chrysanthemum_purchased + roses_purchased + tulips_purchased) >= 20:
        bouquet_price *= 0.80

total_bill = bouquet_price + 2

print(f"{total_bill:.2f}")
