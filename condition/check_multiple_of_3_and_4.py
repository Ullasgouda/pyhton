# Write a program to check whether a number is a multiple of 3 or 5.
num = int(
    input("Enter the number to check whether a number is a multiple of 3 or 5 :  "))
if (num % 3 == 0 and num % 5 == 0):
    print(f"{num} is multiple of 3 and 5")
elif (num % 3 == 0):
    print(f"{num} is multiple of 3")
elif (num % 5 == 0):
    print(f"{num} is multiple of 5")
else:
    print(f"{num} is not a multiple of 3 and 5")
