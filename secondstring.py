#Aine Nic Dhonnacha

# Weekly task 3
# A program that asks a user to input a string
# and outputs every second letter in reverse order. 

# $ python secondstring.py
# Please enter a sentence: The quick brown fox jumps over the lazy dog.
# .o zletrv pu o wr cu h



user_input = (input("Please enter a sentence : "))

#outputs sentence entered by user
print(user_input)

#reverses the sentence
reverse_sentence = user_input[::-1] 	                                                                        

#outputs every second letter in reverse order
print(reverse_sentence[::2])


#references;
#https://www.geeksforgeeks.org/reverse-string-python-5-different-ways/
#https://stackoverflow.com/questions/931092/reverse-a-string-in-python
