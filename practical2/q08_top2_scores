def in_check(x):
    check = False
    while not check:
        numstudents_score = input("Enter %s: " % x)
        try:
            numstudents_score = int(numstudents_score)
            if numstudents_score < 0:
                print("Positive integers only!")
            else:
                return numstudents_score
                check = True
        except ValueError:
            print("Positive integers only!")

def find_max(x, y, z): # x and y are the lists, z specifies first or second highest
    max_score = max(x)
    i = x.index(max_score)
    max_student = y[i]
    if z == 1:
        print("%s has the highest score of %s." % (max_student, max_score))
    elif z == 2:
        print("%s has the second highest score of %s." % (max_student, max_score))
    return i

num_of_students = in_check("number of students")

students = []
scores = []
for student in range(num_of_students):
    student_name = input("Enter student's name: ")
    student_score = in_check("student's score")

    students.append(student_name)
    scores.append(student_score)

if len(students) == 1:
    print("%s is the only student in the list with a score of %s." % (students[0], scores[0]))
else: # I could not think of a solution for multiple students with the same highest score
    position = find_max(scores, students, 1)
    students.pop(position)
    scores.pop(position)
    find_max(scores, students, 2)
