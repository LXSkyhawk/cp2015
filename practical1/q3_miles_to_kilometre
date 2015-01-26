check = False
while check == False:
    miles = input("Enter distance in miles: ")
    if any(c == "." for c in miles) == True and any(c.isdigit() for c in miles) == True:
        miles = float(miles)
        check = True
    elif any(c.isdigit() for c in miles) == True: # to prevent a single "." entered from ruining the code
        miles = float(miles)
        check = True
    else:
        print("Numbers only!")

kilometres = miles * 1.60934
print("It is %skm in kilometres." % round(kilometres, 3))
