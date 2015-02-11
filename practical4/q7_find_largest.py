def find_largest(alist):
    if len(alist) == 1:
        return alist[0]
    else:
        x = find_largest(alist[1:])
        if x > alist[0]:
            return x
        else:
            return alist[0]

int_list = []
check = False
while not check:
    integer = input("Enter integer to add to list. Enter 'end' when finished: ")
    try:
        if integer.lower() == "end":
            check = True
        else:
            integer = int(integer)
            int_list.append(integer)
    except ValueError:
        print("Integers only!")

print(find_largest(int_list))
