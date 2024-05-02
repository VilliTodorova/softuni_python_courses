# The Answer to the Great Question of Life

answer = input('The Answer to the Great Question of Life is...? ')
folded_answer = answer.casefold().strip()
if folded_answer == '42':
    print('Yes')
elif folded_answer == 'forty-two':
    print('Yes')
elif folded_answer == 'forty two':
    print('Yes')
else:
    print('No')
