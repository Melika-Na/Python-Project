sum = 0
num = int (input ('enter your number:'))

while (num > 0) :
    sum = sum + (num % 10)                                
    num = num // 10                                         

print (sum)