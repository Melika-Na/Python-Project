a = int(input ('Enter the number of rows (multipliers):'))
b = int(input ('Enter the number of columns (multiplicands):'))
for i in range (1 ,a):                                   # repetition
    for j in range(1 , b):
        times = (j * i)
        print (j, '*',i , '= ', times , '\n')
    print ("---------------------------")