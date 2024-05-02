bitcoin_amount = int(input())
chinese_yuan_amount = float(input())
commission = float(input())

# •	1 биткойн = 1168 лева.
# •	1 китайски юан = 0.15 долара.
# •	1 долар = 1.76 лева.
# •	1 евро = 1.95 лева.

btc_to_eur = 1168 / 1.95
yuan_to_eur = (0.15 * 1.76) / 1.95

btc_total = bitcoin_amount * btc_to_eur
yuan_total = chinese_yuan_amount * yuan_to_eur
currency_total = btc_total + yuan_total
commission = currency_total * (commission / 100)

result = currency_total - commission

print(f"{result :.2f}")
