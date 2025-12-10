money = input ('How much money do you have? (dollar):')
money = int (money)
print ()

print('100$:\t' , money//100)
money = money % 100
print('50$:\t' , money//50)
money = money % 50
print('20$:\t' , money//20)
money = money % 20
print('10$:\t' , money//10)
money = money % 10
print('5$:\t' , money//5)
money = money % 5
print('1$:\t' , money//1)
money = money % 1
print ()
if money == 0:
    print ("No money left!")
else:
    print("remaining amount :", money)
