#Aine Nic Dhonnacha

#Write a program that takes a positive floating-point number as input 
#and outputs an approximation of its square root. 
#You should create a function called sqrt that does this.

#$ python squareroot.py
#Please enter a positive number: 14.5
#The square root of 14.5 is approx. 3.8.


#Takes a number input from user
float_number = float(input("Please Enter a positive number   "))
print("The number you entered is  : " , float_number)

#function with the name sqrt, which takes one argument and returns its
#approximate square root.                       
def sqrt(number):
    squareroot = (number ** (0.5))
    return squareroot

#Using Newtons method to calculate square root
def newtonSqrt(numberIn, times = 10):
    guess = numberIn * 0.5
    for i in range(times):
        nextGuess = (guess + numberIn/guess) * 0.5
        guess = nextGuess
    return nextGuess

print("The square root of ",str(float_number) + " is  approx. ",  str(round(sqrt(float_number),1)))
print("The Newton Method square root of  ", str(float_number) + " is  approx. ",newtonSqrt(float_number))


#Ref.
#https://runestone.academy/runestone/books/published/thinkcspy/MoreAboutIteration/NewtonsMethod.html
#https://www.w3schools.com/python/python_functions.asp
#https://stackoverflow.com/questions/9595135/how-do-i-calculate-square-root-in-python
#https://stackoverflow.com/questions/20811208/newton-s-method-for-finding-square-roots-in-python
#https://hackernoon.com/calculating-the-square-root-of-a-number-using-the-newton-raphson-method-a-how-to-guide-yr4e32zo
#https://www.programiz.com/python-programming/modules/math
