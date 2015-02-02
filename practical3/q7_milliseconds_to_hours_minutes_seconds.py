def convert_ms(n):
    s = int(n / 1000)
    if s > 60:
        min = int((s - (s % 60)) / 60)
        s = s % 60
        if min > 60:
            h = int((min - (min % 60)) / 60)
            min = min % 60
            print("%s:%s:%s" % (h, min, s))
        else:
            print("0:%s:%s" % (min, s))
    else:
        print("0:0:%s" % s)

check = False
while not check:
    integer = input("Enter number of milliseconds: ")
    try:
        integer = int(integer)
        if integer <= 0:
            print("Positive integers only!")
        else:
            check = True
    except ValueError:
        print("Postive integers only!")

convert_ms(integer)
