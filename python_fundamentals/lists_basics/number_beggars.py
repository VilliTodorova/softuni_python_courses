string_of_money = input().split(", ")
beggars_count = int(input())
integer_of_money = []
for current_money in string_of_money:
    integer_of_money.append(int(current_money))
final_sums = []
start_index = 0
while start_index < beggars_count:
    current_beggar_sum = 0
    for current_index in range(start_index, len(integer_of_money), beggars_count):
        current_beggar_sum += integer_of_money[current_index]
    final_sums.append(current_beggar_sum)
    start_index += 1

print(final_sums)
