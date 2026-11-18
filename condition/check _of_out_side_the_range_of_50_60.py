# Write a program to check whether a number lies outside the range 10 to 50.
num = int(input("Enter the number "))
if num >= 10 and num <= 50:
    print(f"{num} is in range ")
else:
    print(f"{num} is out of range")
