def display_pattern(n):
    list = []
    for times in range(1, n + 1):
        times = str(times)
        list.append(times)

        revlist = []
        for c in reversed(list): # created a separate reversed list so as not to interfere with the main list
            revlist.append(c)
        revlist = " ".join(revlist)

        width = -1 # starts on -1 to account for 1 less whitespace
        for x in range(1, n + 1):
            x = str(x)
            width += len(x)
            width += 1
        print("%s" % revlist.rjust(width))

check = False
while not check:
    integer = input("Enter integer: ")
    try:
        integer = int(integer)
        if integer <= 0:
            print("Positive integers only!")
        else:
            check = True
    except ValueError:
        print("Positive integers only!")

display_pattern(integer)
