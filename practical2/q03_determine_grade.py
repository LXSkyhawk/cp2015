check = False
while not check:
    score = input("Enter score (between 0 and 100 inclusive): ")
    try:
        score = int(score)
        if score < 0 or score > 100:
            print("Invalid! Score must be within 0 and 100.")
        elif score == 100:
            print("Full marks! Straight A, good work!")
            check = True
        elif score >= 70:
            print("Grade is A. Congratulations!")
            check = True
        elif score >= 60:
            print("Grade is B.")
            check = True
        elif score >= 55:
            print("Grade is C.")
            check = True
        elif score >= 50:
            print("Grade is D.")
            check = True
        elif score >= 45:
            print("Grade is E.")
            check = True
        elif score >= 35:
            print("Grade is S.")
            check = True
        elif score >= 0: # I don't feel "safe" putting else
            print("Grade is U.")
            check = True
    except ValueError:
        print("Integers only!")
