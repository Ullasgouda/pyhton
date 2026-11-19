# 20. Check whether a number is a palindrome

num = int(input("Enter the number: "))

temp = num
rev = 0

while temp > 0:
    rem = temp % 10
    rev = rev * 10 + rem
    temp //= 10

if num == rev:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
