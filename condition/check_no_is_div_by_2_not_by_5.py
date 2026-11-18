# Write a program to check whether a number is divisible by 2 but not by 5.
num = int(input(
    "Enter the number to check whether a number is divisible by 2 but not by 5 : "))
if num % 2 == 0 and num % 5 != 0:
    print(f" {num} is divisible by 2 but not by 5")
else:
    print(f"{num} is divisible by both 2 and 5")
