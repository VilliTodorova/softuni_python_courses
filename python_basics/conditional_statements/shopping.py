budget = float(input())
graphic_card_count = int(input())
processor_count = int(input())
ram_memory_count = int(input())
GRAPHIC_CARD = 250.00
DISCOUNT = 0.15

graphic_card_price = graphic_card_count * GRAPHIC_CARD

PROCESSOR = graphic_card_price * 0.35
RAM_MEMORY = graphic_card_price * 0.10

processor_price = processor_count * PROCESSOR
ram_price = ram_memory_count * RAM_MEMORY

total_price = graphic_card_price + processor_price + ram_price

if graphic_card_count > processor_count:
    total_price *= (1 - DISCOUNT)
else:
    pass

leftover = budget - total_price

if leftover >= 0:
    print(f'You have {leftover :.2f} leva left!')
else:
    print(f'Not enough money! You need {abs(leftover) :.2f} leva more!')

