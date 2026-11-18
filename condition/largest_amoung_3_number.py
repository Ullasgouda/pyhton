# Write a program to find the largest among three numbers using nested if.
a = int(input("Enter the 1st number : "))
b = int(input("Enter the 2nd number : "))
c = int(input("Enter the 3ed number : "))
if (a > b):
    if (a > c):
        print(f"{a} is grate ")
if (b > a):
    if (b > c):
        print(f"{b} is grate")
if (c > a):
    if (c > b):
        print(f"{c} is grate")
    else:
        print("all are same ")
