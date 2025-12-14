sum = 0
num = int (input ('enter you number:'))

while (num > 0) :
    sum = sum + (num % 10)                                
    num = num // 10                                         

print (sum)