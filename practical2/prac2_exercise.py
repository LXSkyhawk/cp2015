list = []

check = False

while not check:
    number = input("Enter positive integer to add to list: ")
    try:
        number = int(number)
        if number == -1:
            check = True
        elif number <= 0:
            print("Positive integers only!")
        else:
            list.append(number)
    except ValueError: # I (finally) thought of a better and more effective way of catching errors
        print("Integers only!")

list = sorted(list)
print(list)

x = 0
for integers in list:
    x += integers
print("The total sum of the entered integers is %s." % x)
print("The smallest number in the list is %s." % list[0])
print("The largest number in the list is %s." % list[len(list) - 1])
