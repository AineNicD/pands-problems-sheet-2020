#Write a program that reads	in	two	numbers	and	
# subracts the first one from the second one. 
# The program you print	out	“the difference is 123"
# where 123 is the difference between the numbers.

#Program to substract one number from another.
# input reads out a string so we convert it into an int
# so we can perform mathematical operations.

x = int(input( "Enter first number:"))

y = int(input( "Enter second number:"))

answer = x - y

print( "{} minus {} is {} " .format(x, y, answer))
