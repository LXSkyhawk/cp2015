check = False
while check == False:
    name = input("Enter name: ")
    if name == "":
        print("Enter your name!")
    else:
        check = True

check = False
while check == False:
    hours = input("Enter number of hours worked weekly: ")
    if any(c == "." for c in hours) == True and any(c.isdigit() for c in hours) == True:
        print("Integers only!")
    elif any(c.isdigit() for c in hours) == True:
        hours = float(hours)
        check = True
    else:
        print("Integers only!")

check = False
while check == False:
    pay_rate = input("Enter hourly pay rate: ")
    if any(c == "." for c in pay_rate) == True and any(c.isdigit() for c in pay_rate) == True:
        pay_rate = float(pay_rate)
        check = True
    elif any(c.isdigit() for c in pay_rate) == True: # to prevent a single "." entered from ruining the code
        pay_rate = float(pay_rate)
        check = True
    else:
        print("Numbers only!")

check = False
while check == False:
    cpf_rate = input("Enter CPF contribution rate(%): ")
    if any(c == "." for c in cpf_rate) == True and any(c.isdigit() for c in cpf_rate) == True:
        cpf_rate = float(cpf_rate)
        check = True
    elif any(c.isdigit() for c in cpf_rate) == True:
        cpf_rate = float(cpf_rate)
        check = True
    else:
        print("Integers only!")

gross_pay = round(hours * pay_rate, 2)
cpf_contribution = round(gross_pay * (cpf_rate/100), 2)
net_pay = round(gross_pay - cpf_contribution, 2)

print("Payroll statement for %s" % name)
print("Number of hours worked weekly: %s" % hours)
print("Hourly pay rate: $%s" % pay_rate)
print("Gross pay: $%s" % (gross_pay))
print("CPF contribution at %s percent: $%s" % (cpf_rate, cpf_contribution))
print("Net pay: $%s" % net_pay)
