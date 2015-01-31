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

factors = []

def find_smallest_factors(x):
    if x == 1:
        factors.append(1)
    for number in range(2, 2 * x):
        if number == x: # terminating case
            factors.append(number)
        elif x % number == 0: # recursive case
            factors.append(number)
            y = int(x / number)
            find_smallest_factors(y)
        else:
            continue
        break

find_smallest_factors(integer)
print(factors)
