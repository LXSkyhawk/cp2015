def gcd(m, n):
    if m % n == 0:
        return n
    else:
        return gcd(n, m % n)

def input_check(x):
    check = False
    while not check:
        integer = input("Enter %s positive integer: " % x)
        try:
            integer = int(integer)
            if integer <= 0:
                print("Positive integers only!")
            else:
                return integer
        except ValueError:
            print("Postive integers only!")

check = False
while not check:
    run = input("Run test program or input program? (t/i): ")
    if run == "T" or run == "t":
        print("The greatest common divisor of %s and %s is %s." % (24, 16, gcd(24, 16)))
        print("The greatest common divisor of %s and %s is %s." % (255, 25, gcd(255, 25)))
        check = True
    elif run == "I" or run == "i":
        first_int = input_check("first")
        second_int = input_check("second")
        print("The greatest common divisor of %s and %s is %s." % (first_int, second_int, gcd(first_int, second_int)))
        check = True
