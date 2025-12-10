a = input('enter a: ')
b = input('enter b: ')
c = input('enter c: ')
a = int(a)
b = int(b)
c = int(c)

if (a**2) + (b**2) == (c**2) or (a**2) + (c**2) == (b**2) or (c**2) + (b**2) == (a**2):
    print(' OK')  
else:
    print('Not OK')
