# vCount the number of digits in a given number.
num = int(input("Enter the number : "))
count = 0
i = 1
temp = num
if num == 0:
    count = 1
else:

    while num > 0:
        count += 1
        num = num//10
print(count)
