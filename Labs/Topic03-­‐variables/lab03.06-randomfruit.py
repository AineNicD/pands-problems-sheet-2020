#This program prints out a random fruit.

import random

fruits = ['Apple', 'Pear', 'Orange', 'Bananna']

#we want a random number between 0 and length -1
#index = random.randint (0,len(fruits)-1)

#fruit = fruits[index]

# Code from https://pynative.com/python-random-choice/
fruit = random.choice(fruits)

print( "A Random Fruit: {}" .format(fruit))


#Reference: Andrew Beatty tutorial on moodle
