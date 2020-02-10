# A program that reads in students names
# until the user enters a blank
# and then prints them all out again
# the program prints out all the studens names in a neat way

students = []

Firstname = input("Enter Firstname (blank to quit): ").strip()
while Firstname != "":
    student = {}
    student ["Firstname"] = Firstname
    lastname = input("Enter lastname: ").strip()
    student["lastname"] = lastname
    students.append(student)
    #next student
    Firstname = input("Enter Firstname of next (blank to quit): ").strip()

print ("here are the students you entered:")
for currentStudent in students:
    print ("{} {}".format(currentStudent["Firstname"],currentStudent ["lastname"]))