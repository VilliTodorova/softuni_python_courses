# Ако поръчаните играчки са 50 или повече магазинът прави отстъпка 25% от общата цена.
# От спечелените пари Петя трябва да даде 10% за наема на магазина.
# Да се пресметне дали парите ще ѝ стигнат да отиде на екскурзия.

PUZZLE = 2.60
TALKING_DOLL = 3.00
TEDDY_BEAR = 4.10
MINION = 8.20
TRUCK = 2.00
DISCOUNT = 25 / 100

vacation_cost = float(input())

puzzles_count = int(input())
talking_dolls_count = int(input())
teddy_bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())
total_count = puzzles_count + talking_dolls_count + teddy_bears_count + minions_count + trucks_count

puzzles_total = puzzles_count * PUZZLE
talking_dolls_total = talking_dolls_count * TALKING_DOLL
teddy_bears_total = teddy_bears_count * TEDDY_BEAR
minions_total = minions_count * MINION
trucks_total = trucks_count * TRUCK
income_total = puzzles_total + talking_dolls_total + teddy_bears_total + minions_total + trucks_total

if total_count >= 50:
    income_total = income_total * (1 - DISCOUNT)
else:
    pass

rent_price = income_total * 10 / 100

leftover = income_total - rent_price - vacation_cost

if leftover >= 0:
    print(f'Yes! {leftover :.2f} lv left.')
else:
    print(f'Not enough money! {abs(leftover) :.2f} lv needed.')


# •	Ако парите са достатъчни се отпечатва: "Yes! {оставащите пари} lv left."
# •	Ако парите НЕ са достатъчни се отпечатва: "Not enough money! {недостигащите пари} lv needed."
# Резултатът трябва да се форматира до втория знак след десетичната запетая.
