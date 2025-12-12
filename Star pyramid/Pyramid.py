for i in range (1 , 6):
    for s in range (1, (5 - i) + 1):
        print (" " , end = " ")
    for c in range (1, (2 * i)):
        print ("*", end = " ")
    print ()