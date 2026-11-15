num = int(input("enter your no."))
sum = 0
temp = num
i = 1
while (i < num):
    if (num % i == 0):
        sum = sum+i
    i = i+1
if (sum == temp):
    print("perfect number")
else:
    print("not a perfect number")
