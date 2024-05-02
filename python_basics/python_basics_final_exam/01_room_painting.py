from math import floor, ceil

paint_buckets = int(input())  # 21.50
wallpaper_rolls = int(input())  # 5.20
gloves_price = float(input())   # needed_gloves = ceil(wallpaper_rolls * 0.35)
brush_price = float(input())    # needed_brushes = floor(paint_buckets * 0.48)

needed_gloves = ceil(wallpaper_rolls * 0.35)
needed_brushes = floor(paint_buckets * 0.48)
total_price = paint_buckets * 21.50 + \
              wallpaper_rolls * 5.20 + \
              needed_brushes * brush_price + \
              needed_gloves * gloves_price
delivery_cost = total_price / 15

print(f"This delivery will cost {delivery_cost :.2f} lv.")
