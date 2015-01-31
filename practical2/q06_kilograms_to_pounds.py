pounds = 2.2

print("Kilograms \t Pounds")

for kilogram in range(1, 11):
    print("%s \t\t\t %s" % (kilogram, round(pounds * kilogram, 1)))
