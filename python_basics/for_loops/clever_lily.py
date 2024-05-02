age = int(input())
machine_price = float(input())
toy_price = int(input())
saved_sum = 0
toy_count = 0


for x in range(1, age + 1):
    if x % 2 == 0:
        saved_sum += x * 10 / 2
        saved_sum -= 1
    else:
        toy_count += 1

saved_sum += toy_price * toy_count
difference = saved_sum - machine_price

if difference >= 0:
    print(f"Yes! {difference:.2f}")
else:
    print(f"No! {abs(difference):.2f}")
