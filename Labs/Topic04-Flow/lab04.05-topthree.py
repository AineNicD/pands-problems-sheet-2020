# This program generates 10 random numbers,
# prints them out
# prints out the top 3

# A list is used to store and manipulate the numbers

import random
# programming the general case

howMany = 10
topHowMany = 3
rangeFrom = 0
rangeTo = 100 

numbers = []

for i in range(0,howMany):
    numbers.append(random.randint(rangeFrom,rangeTo))
print ("{} random numbers\t {}".format(howMany,numbers))

# Keeping original list
# The idea to sort and split the list is from stackover flow
# http://stackoverflow.com/q/32296887
topOnes = numbers.copy()
topOnes.sort(reverse = True)
print ("The top {} are \t\t {}".format(topHowMany,topOnes[0: topHowMany]))