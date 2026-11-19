# 25. Find the largest digit in a number.
num = int(input("enter the number : "))
larg = 0
while num > 0:
    rem = num % 10
    if rem > larg:
        larg = rem
    num //= 10
print(larg)
