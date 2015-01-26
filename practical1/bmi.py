# BMI Calculator

print("Calculate your BMI!")
print("Note: BMI calculated may not be accurate for pregnant women, people with muscular build or youths under 18 years of age.")
print("\n")

check1 = False
while check1 == False:
    weight = input("Enter your weight in kilogrammes: ")
    if any(c == "." for c in weight) == True and any(c.isdigit() for c in weight) == True:
        weight = float(weight)
        check1 = True
    elif any(c.isdigit() for c in weight) == True: # to prevent a single "." entered from ruining the code
        weight = float(weight)
        check1 = True
    else:
        print("Numbers only!")

check2 = False
while check2 == False:
    height = input("Enter your height in metres: ")
    if any(c == "." for c in height) == True and any(c.isdigit() for c in height) == True:
        height = float(height)
        check2 = True
    elif any(c.isdigit() for c in height) == True:
        height = float(height)
        check2 = True
    else:
        print("Numbers only!")

user_bmi = weight / (height ** 2)
print("Your BMI is %s." % user_bmi)
if user_bmi < 18.5:
    print("You are at risk of nutritional deficiency diseases and osteoporosis. Do visit a doctor for nutritional advice as soon as possible!")
elif user_bmi < 23.0:
    print("Awesome! You are in the healthy range (lowest risk of weight-related health problems). Keep up the good work!")
elif user_bmi < 27.5:
    print("You are at moderate risk of weight-related health problems. Do keep an eye on your lifestyle!")
elif user_bmi < 50.0:
    print("You are at high risk of weight-related healthy problems! See a doctor for nutritional advice!")
elif user_bmi < 100.0:
    print("Very high risk of health issues!!!")
else:
    print("There must have been an error with your input... or was there?")
