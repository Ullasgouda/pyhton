# 24. Count the number of even and odd digits.
num = int(input("num : "))
i = 1
counte = 0
counto = 0
while i < num:
    if i % 2 == 0:
        counte += 1
    else:
        counto += 1
    i+1
print(counto)
print(counte)
