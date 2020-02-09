#Write a progam that reads in two numbers and divides the first one by the second
#and give the integer result and the remainder.

#Enter first number:{}
#Enter the number you want to divide by:{}
# {} divided by {} with remainder {}

x = int(input("Enter first number: "))
y = int(input ("Enter numer you want to divide by: "))
answer = int(x/y)
remainder = x%y

print(" {} divided by {} is {} with remainder {}" .format ( x, y, answer,remainder))