#Aine Nic Dhonnacha
#Weekly task 4

#A program that asks the user to input any positive integer 
#and outputs the successive values of the following calculation. 
#At each step calculate the next value by taking the current value and, 
#if it is even, divide it by two, but if it is odd, 
#multiply it by three and add one.
#The program will end if the current value is one.

#$ python collatz.py
#Please enter a positive integer: 10
#10 5 16 8 4 2 1


# User enters a positive integer.
number = int(input("Please enter a positive integer: "))

# Using number > 1, so it will continue while the number is bigger than 1. 
while number > 1:
    print (number, end=" ")

    if number % 2 == 0: 
        # number is even
        number = number // 2   

    else:
        # number is odd  
        number = (number * 3) + 1  
         
else:
    print (number, end=" ")      



#references;
#https://www.programiz.com/python-programming/examples/odd-even
#https://docs.python.org/3/tutorial/introduction.html#numbers
#https://docs.python.org/3/tutorial/controlflow.html#if-statements
#https://docs.python.org/3/tutorial/controlflow.html
#https://stackoverflow.com/questions/22130284/python-most-efficient-loop-until-condition











