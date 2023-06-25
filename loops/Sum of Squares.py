#MADE A LIST SO I CAN SEE EACH ELEMENT OF INPUT
squared_num = []
number = int(input('number '))

#I PUT +1 HERE SO I GET THE EXACT NUMBER OF RANGE. RANGE IS BASICALLY -1 FROM THE NUMBER THAT YOU INPUT. EXAMPLE: RANGE (20) = 19.
for num in range(number+1):
    #MADE A VARIABLE TO SQUARED THE NUMBER OF RANGE + INPUT
    squared = num ** 2
    #USED .APPEND HERE TO GET THE ELEMENTS FROM THE LIST
    squared_num.append(squared)

    #USED SUM FUNCTION TO CALCULATE THE SUM OF SQUARED NUMBERS
    answers = sum(squared_num)

    print(answers)
