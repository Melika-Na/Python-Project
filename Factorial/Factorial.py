number = int(input("enter you number: "))

if number < 0:
    print("invalid for negative numbers")
else:
    factorial = 1

for i in range(1, number + 1):
    factorial = factorial * i

print(factorial)