def sum_series1(i):
    if i == 1:
        return 1
    else:
        return ((1 / i) + sum_series1(i - 1))


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

print(sum_series1(integer))
