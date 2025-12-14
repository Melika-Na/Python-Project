for i in range (1 , 6):           # for inputting scores for five classes

    sum = 0
    count = 0               

    while True:
        score = float(input('enter your score:'))
        if score == -1:
            break
        sum += score
        count += 1

    if count > 0 :
        print(count)             # number of scores
        print(sum / count)       # average score