company_name = input()
adult_tickets = int(input())
children_tickets = int(input())  # 30% of net_ticket_price_adults
net_ticket_price_adults = float(input())
service_fee = float(input())    # added to each ticket

# final agency profit is 20% of the total tickets sold
price_children_ticket = net_ticket_price_adults * 0.3
total_agency_profit = (adult_tickets * (net_ticket_price_adults + service_fee) +
                       children_tickets * (price_children_ticket + service_fee)) * 0.2

print(f"The profit of your agency from {company_name} tickets is {total_agency_profit :.2f} lv.")
