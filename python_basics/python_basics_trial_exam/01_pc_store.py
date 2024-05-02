processor_price_dollars = float(input())
graphic_price_dollars = float(input())
ram_price_dollars = float(input())
ram_count = int(input())
discount = float(input())   # in percent

processor_price_leva = processor_price_dollars * 1.57
graphic_price_leva = graphic_price_dollars * 1.57
ram_price_leva = ram_price_dollars * 1.57

total_price = (processor_price_leva * (1 - discount)) + \
              (graphic_price_leva * (1 - discount) +
               ram_price_leva * ram_count)

print(f"Money needed - {total_price :.2f} leva.")
