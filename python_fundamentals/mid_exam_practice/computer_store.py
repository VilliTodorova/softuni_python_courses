command = input()
customer_total_no_tax = 0
discount = 1

while command != 'special' and command != 'regular':
    current_price = float(command)
    if current_price < 0:
        print('Invalid price!')
    else:
        customer_total_no_tax += current_price

    command = input()

if command == 'special':
    discount = 0.9
tax = customer_total_no_tax * 0.2
total_with_tax_discount = (customer_total_no_tax + tax) * discount
if total_with_tax_discount == 0:
    print("Invalid order!")
else:
    print(f"Congratulations you've just bought a new computer!\n"
          f"Price without taxes: {customer_total_no_tax:.2f}$\n"
          f"Taxes: {tax:.2f}$\n"
          f"-----------\n"
          f"Total price: {total_with_tax_discount:.2f}$")
