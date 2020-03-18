#Aine Nic Dhonnacha

#This program calculates somebody's Body Mass Index (BMI).  
#The user inputs the person's height in centimetres and weight in kilograms. 
#The output is their weight divided by their height in metres squared. 

#height will store the value inputed by the user.
height = float(input("Enter persons height in cm: "))

#weight will store the value inputed by the user.
weight = float(input("Enter persons weight in kg: "))

#Bmi calculation
bmi = weight / ((height/100)**2)

#Rounding calculation to 2 decimal places
decimal_places = (round(bmi,2))

print("----------------------------------")

print("Body Mass Index is : ",decimal_places)

print("----------------------------------")


#ref: https://www.includehelp.com/python/bmi-body-mass-index-calculator.aspx
