# Following task lab04.01, 69.5 gets rounded to 70
# This program reads in a students percentage
# and prints out the corresponding grade 
# #https://www.programiz.com/python-programming/methods/built-in/round


percentage = float(input("Enter the percentage: "))
#print (percentage)
percentage = round(percentage)

if percentage  < 0 or percentage > 100:
    print ("Please enter a mu,ner between 0 and 100")
elif percentage < 40:# we know it is greater than 0
    print ("Fail")
elif percentage < 50: #between 40 and 49
    print ("Pass")
elif percentage < 60: # between 50 and 59
    print ("Merit1")
elif percentage < 70: # between 60 and 69
    print ("Merit2") 
else: #the only option left is between 70 and 100
    print ("Distinction")