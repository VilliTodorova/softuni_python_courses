country_list = [country.strip(',') for country in input().split()]
capital_list = [capital.strip(',') for capital in input().split()]

for country, capital in zip(country_list, capital_list):
    print(f'{country} -> {capital}')
