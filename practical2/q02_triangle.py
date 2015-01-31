def in_check(x):
    check = False
    while not check:
        side = input("Enter triangle side %s: " % x)
        try:
            return int(side)
            check = True
        except ValueError:
            print("Integers only!")

side1 = in_check(1)
side2 = in_check(2)
side3 = in_check(3)

if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
    perimeter = side1 + side2 + side3
    print("Perimeter of triangle is %s units!" % perimeter)
else:
    print("Impossible!")
