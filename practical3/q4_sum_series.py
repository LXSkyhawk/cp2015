def m_series(i):
    m = 0
    print("i \t\t m(i)")
    for number in range (1, i + 1):
        m += (number / (number + 1))
        print("%s \t\t %s" % (number, '{0:.4f}'.format(m)))

check = False
while not check:
    run = input("Run test program or input program? (t/i): ")
    if run == "T" or run == "t":
        m_series(20)
        check = True
    elif run == "I" or run == "i":
        check1 = False
        while not check1:
            integer = input("Enter integer: ")
            try:
                integer = int(integer)
                if integer <= 0:
                    print("Positive integers only!")
                else:
                    m_series(integer)
                    check1 = True
                    check = True
            except ValueError:
                print("Positive integers only!")
