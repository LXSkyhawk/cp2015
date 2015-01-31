kilometres = 1.609

print("Miles \t Kilometres \t\t Miles \t Kilometres")

for miles in range(1, 7): # corresponding kilometres for 1-6 miles have only 1 digit before decimal point
    print("%s \t\t %s \t\t\t\t %s \t\t %s" % (miles, round(kilometres * miles, 3), miles + 35, round(kilometres * (miles + 35), 3)))
for miles in range(7, 36):
    if (miles % 10 == 0): # corresponding kilometres for 10, 20 and 30 miles are rounded to 2 decimal places
        print("%s \t\t %s \t\t\t\t %s \t\t %s" % (miles, round(kilometres * miles, 3), miles + 35, round(kilometres * (miles + 35), 3)))
    else:
        print("%s \t\t %s \t\t\t %s \t\t %s" % (miles, round(kilometres * miles, 3), miles + 35, round(kilometres * (miles + 35), 3)))
