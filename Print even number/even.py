a = int(input("first number: "))
b = int(input("second number: "))

if a % 2 == 1:
    a = a + 1

for i in range (a, b + 1, 2):
    print (i , end = " ")