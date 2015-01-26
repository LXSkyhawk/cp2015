check = False
while check == False:
    number = input("Enter an integer between 0 and 1000: ")
    if any(c == "." for c in number) == True and any(c.isdigit() for c in number) == True:
        print("Integers only!")
    elif any(c.isdigit() for c in number) == True:
        check = True
    else:
        print("Integers only!")

x = 0
for digit in number:
    digit = int(digit)
    x += digit
print(x)
