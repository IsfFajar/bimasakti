# Create variable using input
Kilometers = float(input('Enter Distance in Kilometers: '))
Miles = float(input('Enter Distance in Miles: '))

# Convert miles to kilometers and kilometers to miles
Mile_to_Kilometers = Miles * 1.60934
Kilometers_to_Miles = Kilometers / 1.60934

# Print result
print(Miles, 'Miles is: ', round(Mile_to_Kilometers, 3), "Kilometers")
print(Kilometers, 'Kilometers is: ', round(Kilometers_to_Miles, 3), "Mile")