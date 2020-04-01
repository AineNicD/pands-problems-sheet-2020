#Aine Nic Dhonnacha
#Weekly task 7
#A program that reads in a text file and outputs the number of e's it contains.
#The program takes the filename from an argument on the command line.
#$ python es.py moby-dick.txt
#116960

import sys

#from command line 
#program reads a file called mobydick.txt and outputs the number of e's in the document
#read in UTF-8 which the mobydick text is in(previous code was producing an error at a character in the program)
#Unicode has more characters. 

#takes in the name of a file as first argument, second argument is encoding type
with open(sys.argv[1], encoding="utf8") as f:
  
  #reads the document and stores it in variable called text.
  text = f.read()
  #counts the amount of e's in the document and stores them in variable called countE.
  countE = text.count("e")
    
  #displays the quantity of e's in the document. 
  print(countE)



#references;
#https://realpython.com/read-write-files-python/
#https://www.w3schools.com/python/ref_string_count.asp 
#https://www.datacamp.com/community/tutorials/exception-handling-python
#https://docs.python.org/2/library/sys.html





