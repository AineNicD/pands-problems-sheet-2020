#A program that takes a positive floating point number as input and outputs an
#approximate of its square root using a function called sqrt

#Takes a number input from user

float_number = float(input("Please Enter a positive number   "))
print("The number you entered is  : " , float_number)

#function with the name sqrt, which takes one argument and returns its
#approximate square root.                       
def sqrt(number):
    squareroot = (number ** (0.5))
    return squareroot

#ref: https://runestone.academy/runestone/books/published/thinkcspy/MoreAboutIteration/NewtonsMethod.html
#Using Newtons method to calculate square root
def newtonSqrt(numberIn, times = 10):
    guess = numberIn * 0.5
    for i in range(times):
        nextGuess = (guess + numberIn/guess) * 0.5
        print(i)#this is the iterator (loop) so that I can see what loop am I on
        print(guess)#this is the guess in this loop
        
        guess = nextGuess#this takes the new guess and puts it in variable guess
    return nextGuess

print("The square root of ",str(float_number) + " is  approx. ",  str(round(sqrt(float_number),2)))
print("The Newton Method square root of  ", str(float_number) + " is  approx. ",newtonSqrt(float_number))
