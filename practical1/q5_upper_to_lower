check = False
while check == False:
    letter = input("Enter an uppercase letter: ")
    if letter == letter.lower():
        print("One uppercase letter only!")
    elif any(c.isalpha() for c in letter) == True:
        check = True
    else:
        print("One uppercase letter only!")

print("The corresponding lowercase letter is %s." % chr(ord(letter) + 32))
