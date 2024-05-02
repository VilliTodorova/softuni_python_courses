while True:
    your_input = float(input())

    if your_input < 0:
        print("Negative number!")
        break

    your_input *= 2
    print(f"Result: {your_input:.2f}")
