def find_num_uppercase(str):
    if len(str) == 1:
        if ord(str) >= 65 and ord(str) <= 90:
            return 1
        else:
            return 0
    else:
        if ord(str[len(str) - 1]) >= 65 and ord(str[len(str) - 1]) <= 90:
            return 1 + find_num_uppercase(str[:-1])
        else:
            return find_num_uppercase(str[:-1])

string = input("Enter string: ")

print(find_num_uppercase(string))
