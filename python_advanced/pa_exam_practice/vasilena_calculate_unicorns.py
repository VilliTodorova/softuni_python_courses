while True:
    name = input("What's your name? (type 'end' to exit the program) ")

    if name.lower() == "end":
        break

    if name.lower() == "vasilena":
        print(f"{name}, You always win, my love! I found 99999 unicorns in your closet.")

    try:
        magic = int(input(f"{name}, please enter your magic level: "))

        if magic <= 0:
            print("This is sad, Karen! I didn'project find any unicorns in your closet. :(")
        elif 0 < magic < 10:
            print(f"{name} - Мътнород. 1 тъжен еднорог в гардероба ти, който пърди тъжни дъги.")
        elif 10 <= magic < 100:
            print(f"{name}, билетът ти за Хогуортс сигурно е на път. "
                  "Хванах 2 еднорога в гардероба ти да правят секс. Скоро ще имаш 3.")
        else:
            print(f"Dumbledore! Десетки еднорози правят бесен купон в твоя гардероб.")

    except ValueError:
        print("Invalid data. Must be a number!")


