num = int(input("Enter a number: "))
# by usling the length of the string representation of the number to determine if it is single, double, or more than three digits.
if (num == int(str(num)[0:1:1])):
    print(f"The number {num} is single")
elif (num == int(str(num)[0:2:1])):
    print(f"The number {num} is 2")
else:
    print(f"The number {num} is more than 3")
# by using and finding the number of digits in the number to determine if it is single, double, or more than three digits.
if (num > 1 and num < 10):
    print(f"The number {num} is single")
elif (num > 9 and num < 100):
    print(f"The number {num} is 2")
else:
    print(f"The number {num} is more than 3")
# by using the length of the string representation of the number to determine if it is single, double, or more than three digits.
if (len(str(num)) == 1):
    print(f"The number {num} is single")
elif (len(str(num)) == 2):
    print(f"The number {num} is 2")
else:
    print(f"The number {num} is more than 3")
