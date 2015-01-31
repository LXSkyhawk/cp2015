check = False
while not check:
    year = input("Enter year: ")
    try:
        year = int(year)
        check = True
    except ValueError:
        print("Integers only!")

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("%s is a leap year." % year)
else:
    print("%s is not a leap year." % year)
