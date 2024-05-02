name = input('Въведи име или дума: ')
length_of_word = len(name)
print('\n'.join([''.join([(name[(x-y) % length_of_word]
                           if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else' ')
                          for x in range(-30, 30)])for y in range(15, -15, -1)]))
