# 18. Find the product of digits of a number.
n = int(input("number: "))
temp = 1
while n > 0:
    rem = n % 10
    temp *= rem
    n //= 10
print(temp)
