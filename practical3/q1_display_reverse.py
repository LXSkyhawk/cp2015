def reverse_int(n):
    list = []
    n = str(n)
    for c in n:
        list.append(c)
    list.reverse()
    revn = "".join(list)
    print(revn)

check = False
while not check:
    integer = input("Enter integer: ")
    try:
        integer = int(integer)
        if integer < 0:
            print("Non-negative integers only!")
        else:
            check = True
    except ValueError:
        print("Non-negative integers only!")

reverse_int(integer)
