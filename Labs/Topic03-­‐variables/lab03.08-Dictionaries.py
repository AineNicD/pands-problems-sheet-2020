# Create a Dictionary Object called currentBook that has 3 attributes
# . Title
# . Author
# . Price

# As an exercise 
# Print out the dictionary object
# Print just the author of the currentBook
# Create a new attribute called ISBN (with some value)
# Print out all the values in the currentBook (using for loop)

currentBook = {
    "Title" : "Harry potter and the cursed child",
    "Author": "J K Rowling",
    "Price" : 20

}
#print dictionary object
print (currentBook)

#print just the author
print (currentBook["Author"])

#create and set attributes ISBN
currentBook [ "ISBN"] = "9788498387568"

#user for loop to iterate through the currentBook's values
#notice the order the for loop gives the values.

print ("the current book has these values:")
for value in currentBook.values():
    print( " => {} " .format(value))
    
    
#Reference: Andrew Beatty tutorial on moodle
