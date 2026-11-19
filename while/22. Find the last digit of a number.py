# 22. Find the last digit of a number.

num = int(input("Enter the number: "))

while num >= 10:
    rem = num % 10
    break

print("Last digit:", rem)
