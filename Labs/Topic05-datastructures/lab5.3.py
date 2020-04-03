#Create a program that puts 10 random numbers into a queue(list), the
#program should then output all the values in the queue, then take the
#numbers from the queue one at a time, print it and the current numbers still
#in the queue. (the command pop(0) takes the first element out of a list)

#ref: code provided in course document by Andrew Beatty.

import random

#create an empty queue
queue = []

#create a variable for the number of values in the queue
numberOfNumbers=10

#range of numbers for the queue, up to 100
rangeTo=100


#Loop that begins at 0 up to the number of values in the queue
for n in range(0,numberOfNumbers):
   #appends a random number of 10 numbers as specified in rangeTo variable
    queue.append(random.randint(0,rangeTo))

#displays the queue
print ("queue is {}".format(queue))

#while loop that runs while the queue length is not equal to 0, ie: while not empty 
while len(queue) != 0:
    
    #currentNumber is the queue with first number popped.
    currentNumber = queue.pop(0)
    
    #displays the current number and the queue
    print ("current Number is {} and the queue is {} ".format(currentNumber, queue))

print ("the queue is now empty")

# Reference: Code from Andrew Beatty lab sheet on moodle
