sum = 0                                        # Counter to count the number of digits.
num = int (input ('enter you number:'))

while (num > 0) :
    print (num % 10)                           # Extract and print the last digit.
    num = num // 10                            # Remove the last digit from the number.           
    sum = sum + 1

print ('\n','digits :'  , sum)