check = False
while check == False:
    ascii = input("Enter ASCII Code (Integer between 0 and 127): ")
    if any(c == "." for c in ascii) == True:
        print("An integer between 0 and 127 only!")
    elif any(c.isdigit() for c in ascii) == True:
        ascii = int(ascii)
        if ascii >= 0 and ascii <= 127:
            check = True
        else:
            print("An integer between 0 and 127 only!")
    else:
        print("An integer between 0 and 127 only!")

print("The corresponding character is '%s'." % chr(ascii))
