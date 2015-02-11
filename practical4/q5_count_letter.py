def count_letter(str, ch):
    str = str.lower()
    ch = ch.lower()
    if len(str) == 1:
        if str[0] == ch:
            return 1
        else:
            return 0
    elif str[len(str) - 1] == ch:
        return 1 + count_letter(str[:-1], ch)
    else:
        return count_letter(str[:-1], ch)

string = input("Enter string: ")
character = input("Enter wanted character: ")

print(count_letter(string, character))
