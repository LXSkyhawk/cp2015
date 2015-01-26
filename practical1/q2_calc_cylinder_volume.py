import math

check1 = False
while check1 == False:
    radius = input("Enter radius of the cylinder: ")
    if any(c == "." for c in radius) == True and any(c.isdigit() for c in radius) == True:
        radius = float(radius)
        check1 = True
    elif any(c.isdigit() for c in radius) == True: # to prevent a single "." entered from ruining the code
        radius = float(radius)
        check1 = True
    else:
        print("Numbers only!")

check2 = False
while check2 == False:
    length = input("Enter length of the cylinder: ")
    if any(c == "." for c in length) == True and any(c.isdigit() for c in length) == True:
        length = float(length)
        check2 = True
    elif any(c.isdigit() for c in length) == True:
        length = float(length)
        check2 = True
    else:
        print("Numbers only!")

area = radius * radius * math.pi
volume = area * length
print("The volume of the cylinder is %sunits^3." % round(volume, 3))
