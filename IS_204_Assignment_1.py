# %%
#Benjamin DePew
#8/29/2022
#IS-204-QL

#These variables recieve the user's input for their car's make, year, and model

Make = input("Enter your car make: ")
Model = input("Enter your car model: ")
Year = input("Enter your car year: ")

#This recives the miles driven and the amount of fuel used in gallons

miles = input("Enter how many miles you drove: ")
m = float(miles)

gallons = input("Enter how many gallons you used as a decimal: ")
g= float(gallons)

#This computes miles per gallon

mpg = (m/g)

#This prints the car's make, year, and model

print(Make, Model, Year)

#This prints the average MPG

print(mpg)

input('Press ENTER to exit')


