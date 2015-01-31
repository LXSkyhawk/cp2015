check = False
n = 100
while not check:
    if n ** 3 < 12000:
        print(n)
        check = True
    else:
        n -= 1
