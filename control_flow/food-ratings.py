#MY ANSWER
stars = float(input('Give me rating from 1 to 5 '))

if stars >= 4.5:
  print('Extraordinary')

elif stars >= 4:
  print('Excellent')

elif stars >= 3:
    print('Good')
elif stars >= 2:
    print('Fair')

else:
    print('poor')

#CODEDEX'S ANSWER

rating = float(input('Give me rating from 1 to 5 '))

options = {
    (4.5, 5): "Extraordinary",
    (4, 4.5): "Excellent",
    (3, 4): "Good",
    (2, 3): "Fair",
    (0, 2): "Poor"
}

for key in options:
    if key[0] < rating <= key[1]:
        print(options[key])