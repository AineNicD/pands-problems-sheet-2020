#this program calcualtes how many tiles you will need
#when tiling a wall or floor (in m2).

length= float(input ("enter room length: "))
width =float(input ("enter room width: "))

area = length * width
needed = area * 1.05

print("you need", needed, "tiles in metres squared.")



ref: Ian McLoughlin
