#Write a program that reads in a string and strips any leading or trailing spaces,
#The pogram should also convert the string to lower case.
#The program should also output the length of the input and output strings.


rawString = input ("Please enter a string:" )
normalisedString  = rawString.strip() .lower()

LengthofRawString = len (rawString)
LengthofNormalisedString = len (normalisedString)

print ("That String normalised is : {} ".format (normalisedString) )
print ("We reduced the input string from {} to {} characters" .format (LengthofRawString, LengthofNormalisedString))