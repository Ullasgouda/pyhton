# 17. Find the sum of digits of a number.
n = int(input("number: "))
temp = 0
while n > 0:
    rem = n % 10
    temp += rem
    n //= 10
print(temp)
