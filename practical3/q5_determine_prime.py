def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    return True

def get_integer():
    check = False
    while not check:
        integer = input("Enter integer: ")
        try:
            integer = int(integer)
            if integer <= 0:
                print("Positive integers only!")
            else:
                return integer
                check = True
        except ValueError:
            print("Positive integers only!")

check = False
while not check:
    run = input("Display first thousand prime numbers or run input program? (d/i): ")
    if run == "D" or run == "d":
        number = 1 # starting number
        count = 0 # count of how many prime numbers
        list = []
        while count <= 1000:
            truefalse = is_prime(number)
            if truefalse == True:
                list.append(str(number)) # appending string of prime numbers into the list
                if len(list) == 10: # when there are 10 items in the list; print out and reset
                    list = " ".join(list)
                    print(list)
                    list = []
                count += 1 # if prime, increase count by 1
            number += 1 # move on to next number
        check = True

    elif run == "I" or run == "i":
        input_integer = get_integer()
        input_integer = int(input_integer)
        print(is_prime(input_integer))
        check = True
