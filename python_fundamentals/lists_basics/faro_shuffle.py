deck_cards = input().split()
shuffles_count = int(input())

for shuffle in range(shuffles_count):
    deck_middle = len(deck_cards) // 2
    left_part = deck_cards[0:deck_middle]
    right_part = deck_cards[deck_middle:]
    deck_after_shuffle = []
    for card_index in range(len(left_part)):
        deck_after_shuffle.append(left_part[card_index])
        deck_after_shuffle.append(right_part[card_index])
    deck_cards = deck_after_shuffle
print(deck_after_shuffle)
