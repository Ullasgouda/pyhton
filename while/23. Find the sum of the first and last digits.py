# 23. Find the sum of the first and last digits.
num = int(input("Enter the  number : "))
temp1 = num
temp2 = num
rem = 0
while temp1 > 10:
    temp1 //= 10
while temp2 > 10:
    rem = temp2 % 10
    break
sum = temp1+rem
print(f"Sum of first and last is {sum}")
