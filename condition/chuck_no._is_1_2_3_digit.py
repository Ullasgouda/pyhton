# Write a program to check whether a number is two-digit, three-digit, or more.
num = int(input("Enter the number : "))
num1 = len(str(num))
if num1 == 1:
    print("The number is one-digit")
elif num1 == 2:
    print("The number is two_digit")
elif num1 == 3:
    print("The number is three_digit")
else:
    print("The number is more the three_digit")
