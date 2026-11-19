# 21. Find the first digit of a number.
num = int(input("number : "))
while num > 10:

    num //= 10
print(num)
