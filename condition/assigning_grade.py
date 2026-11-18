# . Write a program to assign grades:
#  90+ → A
#  75–89 → B
#  50–74 → C
#  Below 50 → Fail
marks = int(input("Enter the marks : "))
if (marks >= 90):
    print("You r getting A grade ")
elif (marks >= 75 and marks <= 89):
    print("You r getting b grade ")
elif (marks >= 50 and marks <= 74):
    print("You r getting c grade")
elif (marks < 50):
    print("you r fail")
else:
    print("You had entered the invalid marks ")
