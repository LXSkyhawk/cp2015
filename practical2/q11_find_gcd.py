def in_check(x):
    check = False
    while not check:
        integer = input("Enter %s integer: " % x)
        try:
            integer = int(integer)
            if integer <= 0:
                print("Positive integers only!")
            else:
                return integer
                check = True
        except ValueError:
            print("Positive integers only!")

integer1 = in_check("first")
integer2 = in_check("second")

first_list = []
second_list = []

for number in range(1, integer1 + 1): # finding the factors of the integers
    if integer1 % number == 0:
        first_list.append(number)
for number in range(1, integer2 + 1):
    if integer2 % number == 0:
        second_list.append(number)

common_divisors = []

for divisor1 in first_list:
    for divisor2 in second_list:
        if divisor1 == divisor2:
            common_divisors.append(divisor1)

print("The greatest common divisor of %s and %s is %s." % (integer1, integer2, max(common_divisors)))
