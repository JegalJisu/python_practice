fruit = 'banana'
print('n' in fruit)
print('m' in fruit)
print('nan' in fruit)
if 'A' in fruit :
    print('Found it!')

word = 'apple'
if word < fruit :
    print('Your word, ' + word + ', comes before banana.')
elif word > fruit :
    print('Your word, ' + word + ',comes after banana.')
else :
    print('All right, bananas.')