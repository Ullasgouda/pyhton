m1 = int(input("Enter marks for subject 1: "))
m2 = int(input("Enter marks for subject 2: "))
m3 = int(input("Enter marks for subject 3: "))
m4 = int(input("Enter marks for subject 4: "))
m5 = int(input("Enter marks for subject 5: "))
m6 = int(input("Enter marks for subject 6: "))
if (m1 <= 100 and m2 <= 100 and m3 <= 100 and m4 <= 100 and m5 <= 100 and m6 <= 100):
    total = m1+m2+m3+m4+m5+m6
else:
    print("Please enter valid marks")
percentage = ((total/6))
if (percentage >= 90):
    print(f"Your percentage is {percentage} and your grade is A")
elif (percentage >= 80 and percentage < 90):
    print(f"Your percentage is {percentage} and your grade is B")
elif (percentage >= 70 and percentage < 80):
    print(f"Your percentage is {percentage} and your grade is C")
elif (percentage >= 60 and percentage < 70):
    print(f"Your percentage is {percentage} and your First class")
elif (percentage >= 50 and percentage < 60):
    print(f"Your percentage is {percentage} and your Second class")
else:
    print(f"Your percentage is {percentage} and your Fail")
