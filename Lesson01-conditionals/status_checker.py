# Student Information System - Starter Code

print("STUDENT INFORMATION SYSTEM")
print("========================================")

# Get student information
name = input("Enter student name: ")
age = int(input("Enter student age: "))
gpa = float(input("Enter student GPA (0.0-4.0): "))

# Show student information
print()
print("Student Information:")
print("Name:", name)
print("Age:", age)
print("GPA:", gpa)
print()
print('eligibility status')
# TODO: Check if age is valid (between 16 and 100)
if 16<=age<=100:
    

# TODO: Check if GPA is valid (between 0.0 and 4.0)
    if 0.0<=gpa<=4.0:

# TODO: Check enrollment eligibility (age >= 18 AND gpa >= 2.0)
        if age>=18 and gpa>=2.0:
            print('eligible for enrollment')
        else:
            print('not eligible for enrolment')

# TODO: Check voting eligibility (age >= 18)
        if age >=18:
            print('eligible for voting')
        else:
            print('inelligible for voting')

# TODO: Check honor roll status (gpa >= 3.5)
        if gpa>=3.5:
            print('honor roll')
        else:
            print('not on honor roll')
    else:
        print('enter valid num for gpa')
else:
    print('invalid num for age')