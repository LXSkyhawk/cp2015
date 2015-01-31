def in_check(x):
    check = False
    while not check:
        month_year = input("Enter %s in integer form: " % x)
        try:
            return int(month_year)
            check = True
        except ValueError:
            print("Integers only!")

month = in_check("month")
year = in_check("year")

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

month_name = months[month - 1]

if month_name == "February":
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("February %s has 29 days." % year)
else:
    print("%s %s has %s days." % (month_name, year, days[month - 1]))
