def reverse_int(n):
    if len(n) == 1:
        return n
    else:
        return n[len(n) - 1] + reverse_int(n[:-1])

check = False
while not check:
    integer = input("Enter non-negative integer: ")
    try:
        integer = int(integer)
        if integer < 0:
            print("Non-negative integers only!")
        else:
            integer = str(integer)
            check = True
    except ValueError:
        print("Non-negative integers only!")

print(reverse_int(integer))
