# Create variable using if-else input
while True: 
    Kilometers_input = input('Enter Distance in Kilometers: ')
    if Kilometers_input.isnumeric(): # 
        Kilometers = float(Kilometers_input)
        break
    else:
        print('Invalid input. Please input valid number')

while True:
    Miles_input = input('Enter Distance in Miles: ')
    if Miles_input.isnumeric():
        Miles = float(Miles_input)
        break
    else:
        print('Invalid input. Please input valid number')

# Convert miles to kilometers and kilometers to miles
Mile_to_Kilometers = Miles * 1.60934
Kilometers_to_Miles = Kilometers / 1.60934

# Print result
print(Miles, 'Miles is: ', round(Mile_to_Kilometers, 3), "Kilometers")
print(Kilometers, 'Kilometers is: ', round(Kilometers_to_Miles, 3), "Miles")