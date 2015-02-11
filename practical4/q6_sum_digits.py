def sum_digits(n):
    if len(n) == 1:
        return int(n)
    else:
        return int(n[len(n) - 1]) + sum_digits(n[:-1])

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

print(sum_digits(integer))
