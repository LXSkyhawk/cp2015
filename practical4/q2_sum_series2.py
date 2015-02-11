def sum_series2(i):
    if i == 1:
        return 1/3
    else:
        return ((i / (2 * i + 1)) + sum_series2(i - 1))


check = False
while not check:
    integer = input("Enter positive integer: ")
    try:
        integer = int(integer)
        if integer <= 0:
            print("Positive integers only!")
        else:
            check = True
    except ValueError:
        print("Postive integers only!")

print(sum_series2(integer))
