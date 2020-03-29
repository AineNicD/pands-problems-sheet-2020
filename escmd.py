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

with open(sys.argv[1], encoding="utf8") as f:
  text = f.read()
  countE = text.count("e")
    
  print(countE)



#references;
#https://realpython.com/read-write-files-python/
#https://www.w3schools.com/python/ref_string_count.asp 
#https://www.datacamp.com/community/tutorials/exception-handling-python
#https://docs.python.org/2/library/sys.html





