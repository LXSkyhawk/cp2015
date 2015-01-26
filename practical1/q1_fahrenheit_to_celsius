check = False
while check == False:
    fahrenheit = input("Enter temperature in Fahrenheit: ")
    if any(c == "." for c in fahrenheit) == True and any(c.isdigit() for c in fahrenheit) == True:
        fahrenheit = float(fahrenheit)
        check = True
    elif any(c.isdigit() for c in fahrenheit) == True: # to prevent a single "." entered from ruining the code
        fahrenheit = float(fahrenheit)
        check = True
    else:
        print("Numbers only!")

celsius = (5/9) * (fahrenheit - 32)
print("It is %s°C in Celsius." % celsius)
