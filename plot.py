#Aine Nic Dhonnacha
#Weekly task 8

#A program that displays a plot of the functions 
#f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.

#Type ipython into command line.
#Type %logstart to activate auto-logging.

#When working with plots, import numpy
#numpy provides a data structure when working with numberical data
import numpy as np

#matplotlib.pyplot helps us create plots when working with numberical data
import matplotlib.pyplot as plt

#.arange() can take 1, 2, or 3 numbers as input and will provide you with lists based on the numbers
#that you have input as arguments

#note: python's range() command will only give you integers, numpy's arange() command will give you float
#range [0, 4] on the one set of axes.
x = np.arange(0.0,5.0,1.0)

#display the numpy array
x

#g(x)= x2
g1 = x ** 2

#display g1
g1

#h(x)=x3
h1 = x ** 3

#display h
h1

#plot x in green line
plt.plot(x, x, 'g', label="x")

#plot x2 in blue line 
plt.plot(x, g1, 'b', label="x2")

#plot x3 in yellow line
plt.plot(x, h1, 'y', label="x3")

#add a legend to plot
plt.legend()

#add title
plt.title('f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] ', fontsize=18)

#show the plot
plt.show()


# References;
# Moodle Course video on plots which is very good and gave a solid understanding of how to start creating plots
# https://numpy.org/
# https://matplotlib.org/api/pyplot_summary.html
# https://realpython.com/python-matplotlib-guide/

