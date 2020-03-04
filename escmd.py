#Aine Nic Dhonnacha
#Weekly task 7
#Write a program that reads in a text file and outputs the number of e's it contains.
#The program should take the filename from an argument on the command line.
#$ python es.py moby-dick.txt
#116960

import sys

#from command line 
#program reads a file call mobydick.txt and outputs the number of e's in the document
#read in UTF-8 which the mobydick text is in(code was producing error at a character in the program)
#Unicode has more characters. 
with open(sys.argv[1], encoding="utf8") as f:
  text = f.read()
  countE = text.count("e")
    
  print(countE)



#ref
#https://realpython.com/read-write-files-python/
#https://www.w3schools.com/python/ref_string_count.asp 
#https://www.datacamp.com/community/tutorials/exception-handling-python
#https://docs.python.org/2/library/sys.html





