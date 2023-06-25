#THIS IS NOT FINISH YET

import random

#GET THE INPUT
dice1 = int(input('What is the total (2-12)? ' ))

#MAKING TOTAL VARIABLE TO 0
total = 0

#AS LONG AS (dice1) AND (total) ARE NOT EQUAL, IT WILL KEEPS LOOPING
while dice1 != total:

    #SETTING THE RANDOMINT FROM 1 TO 6
    rand1 = random.randint(1, 6)
    rand2 = random.randint(1, 6)
    #GETTING THE SUM OF (RAND1) AND (RAND2)
    total = rand1 + rand2

    #JUST GETTING THE INFO
    print("Dice 1:", rand1)
    print("Dice 2:", rand2)
    print("Total:", total)

    #IF THE ANSWER IS NOT CORRENT, THE INPUT WILL BE ASK AGAIN.
    dice1 = int(input('What is the total (2-12)? ' ))

    #IF YOU ANSWER IS CORRENT, IT WILL PRINT 'NICE'
if dice1 == total:
    print('Nice!')




