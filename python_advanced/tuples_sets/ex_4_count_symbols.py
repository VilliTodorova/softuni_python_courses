your_text = input()

for char in sorted(set(your_text)):
    print(f"{char}: {your_text.count(char)} time/s")
