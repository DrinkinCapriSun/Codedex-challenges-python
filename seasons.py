#MY ANSWER
month = int(input('Month number? '))

#Can't use comma when comparing multiple number, so use or/and.
if month == 1 or month == 2 or month == 3:
  print('Winter')
elif month == 4 or month == 5 or month == 6:
  print('Spring')
elif month == 7 or month == 8 or month == 69:
  print('Summer')
elif month <= 12:
  print('Autumn')
else:
  print('Invalid')

#CODEDEX'S ANSWER
month = int(input('Month number? '))
#KINDA WEIRD, CUZ THEY ASKED TO USE 'OR'
if 1 <= month <= 3:
  print('Winter ❄️')
elif 4 <= month <= 6:
  print('Spring 🌱')
elif 7 <= month <= 9:
  print('Summer 🌻')
elif 10 <= month <= 12:
  print('Autumn 🍂')
else:
  print('Invalid input!')