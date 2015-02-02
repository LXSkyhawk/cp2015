import random

def print_matrix(n):
    count1 = 0
    while count1 < n:
        list = []
        count2 = 0
        while count2 < n:
            rand_integer = random.randint(0, 1)
            list.append(str(rand_integer))
            count2 += 1
        print(" ".join(list))
        count1 += 1

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
        print("Postive integers only!")

print_matrix(integer)
