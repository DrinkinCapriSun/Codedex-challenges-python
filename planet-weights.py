#MY ANSWER
earth = float(input('what is your weight in Earth? '))
#PLANET VARIABLE HAS NO USE HERE, IDK WHY THEY EVEN ASKED TO WRITE AN INPUT.
planet = float(input('Number that correlates with a planet? '))

#CREATING A VARIABLE TO GET THE WEIGHT ON ANOTHER PLANET BASICALLY THE TOTAL WEIGHT
destination_weight1 = earth *  0.38
destination_weight2 = earth *  0.91
destination_weight3 = earth *  0.38
destination_weight4 = earth *  2.53
destination_weight5 = earth *  1.07
destination_weight6 = earth *  0.89
destination_weight7 = earth *  1.14

#I CREATED A VARIABLE PREVIOUSLY SO THAT I CAN COMPARE IT TO THE TOTAL WEIGHT WHICH IS BASICALLY THE DATA INSIDE THE VARIABLE PREVIOUSLY.
if destination_weight1 == earth * 0.38:
  print('Mercury')
elif destination_weight2 == earth * 0.91:
    print('Venus')
elif destination_weight2 == earth * 0.38:
    print('Mars')
elif destination_weight2 == earth * 2.53:
    print('Jupiter')
elif destination_weight2 == earth * 1.07:
    print('Saturn')
elif destination_weight2 == earth * 0.89:
    print('Uranus')
else:
    print('Neptune')


#CODEDEX'S ANSWER
earth = float(input('What is your weight in Earth? '))
planet = int(input('Enter the number that correlates with a planet: '))

destination_weight1 = earth *  0.38
destination_weight2 = earth *  0.91
destination_weight3 = earth *  0.38
destination_weight4 = earth *  2.53
destination_weight5 = earth *  1.07
destination_weight6 = earth *  0.89
destination_weight7 = earth *  1.14

switcher = {
    1: "Mercury",
    2: "Venus",
    3: "Earth",
    4: "Mars",
    5: "Jupiter",
    6: "Saturn",
    7: "Uranus",
    8: "Neptune"
}

destination = switcher.get(planet, "Invalid planet selection")
if destination == "Invalid planet selection":
    print(destination)
else:
    destination_weight = locals()['destination_weight' + str(planet)]
    print("Your weight on " + destination + " is " + str(destination_weight))