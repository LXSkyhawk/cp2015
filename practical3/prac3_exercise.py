import random

def linear_search(A):
    check = False
    while not check:
        target_integer = input("Enter integer to be found in list: ")
        try:
            target_integer = int(target_integer)
            check = True
        except ValueError:
            print("Integers only!")
    num = 0
    for i in range(len(A)):
        if A[i] == target_integer:
            print("%s was found at position %s." % (target_integer, i))
            num += 1
    if num == 0:
        print("%s could not be found in list." % target_integer)
    else:
        print("%s was found a total of %s times in list." % (target_integer, num))


check = False
while not check:
    num_integers = input("Enter total number of integers: ")
    try:
        num_integers = int(num_integers)
        if num_integers <= 0:
            print("Positive integers only!")
        else:
            check = True
    except ValueError:
        print("Postive integers only!")

integers = []

check = False
while not check:
    input_random = input("Are the integers to be inputted by user or randomly generated? (i/r): ")
    if input_random == "I" or input_random == "i":
        for x in range(num_integers):
            check = False
            while not check:
                integer = input("Enter integer: ")
                try:
                    integer = int(integer)
                    integers.append(integer)
                    check = True
                except ValueError:
                    print("Integers only!")
    elif input_random == "R" or input_random == "r":
        print("Integers generated will be within -1000 to 1000.")
        for x in range(num_integers):
            y = random.randint(-1000, 1000)
            integers.append(y)
        check = True

linear_search(integers)
