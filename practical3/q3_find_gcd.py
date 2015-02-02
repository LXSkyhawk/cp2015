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

def gcd(m, n):
    first_list = []
    second_list = []

    for number in range(1, m + 1): # finding the factors of the integers
        if m % number == 0:
            first_list.append(number)
    for number in range(1, n + 1):
        if n % number == 0:
            second_list.append(number)

    common_divisors = []

    for divisor1 in first_list:
        for divisor2 in second_list:
            if divisor1 == divisor2:
                common_divisors.append(divisor1)

    print("The greatest common divisor of %s and %s is %s." % (m, n, max(common_divisors)))

check = False
while not check:
    run = input("Run test program or input program? (t/i): ")
    if run == "T" or run == "t":
        gcd(24, 16)
        gcd(255, 25)
        check = True
    elif run == "I" or run == "i":
        integer1 = in_check("first")
        integer2 = in_check("second")
        gcd(integer1, integer2)
        check = True
