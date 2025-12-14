num = int (input ('enter your number:'))

reverse = 0
while (num > 0) :
    reverse = (reverse * 10) + (num % 10)
    ''' 
1. num % 10 -> Extract the last digit of the current number.
   Example: if num = 123, then num % 10 = 3
2. reverse * 10 -> Shift the existing digits of 'reverse' one place to the left (multiply by 10).
   Example: if reverse = 12, then reverse * 10 = 120
3. Add the last digit of num to the shifted reverse.
  Example: 120 + 3 = 123
4. Assign the result back to 'reverse', so it gradually builds the reversed number.
'''

    num = num // 10                           # Remove the last digit from num

print (reverse)