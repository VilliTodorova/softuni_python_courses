city = input()
sales_volume = float(input())
commission = 0

sales_percentage = {
    "Sofia": {
        "0-500": 0.05,
        "501-1000": 0.07,
        "1001-10000": 0.08,
        "10001+": 0.12
    },
    "Varna": {
        "0-500": 0.045,
        "501-1000": 0.075,
        "1001-10000": 0.10,
        "10001+": 0.13
    },
    "Plovdiv": {
        "0-500": 0.055,
        "501-1000": 0.08,
        "1001-10000": 0.12,
        "10001+": 0.145
    }
}

if city not in sales_percentage or sales_volume < 0:
    print("error")
    exit()
else:
    if sales_volume <= 500:
        commission = sales_percentage[city]["0-500"] * sales_volume
    elif sales_volume <= 1000:
        commission = sales_percentage[city]["501-1000"] * sales_volume
    elif sales_volume <= 10000:
        commission = sales_percentage[city]["1001-10000"] * sales_volume
    else:
        commission = sales_percentage[city]["10001+"] * sales_volume

print(f"{commission:.2f}")
