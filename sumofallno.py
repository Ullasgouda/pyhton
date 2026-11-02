num = int(input("enter the no."))
sum = 0
while (num > 0):
    i = num % 10
    sum += i
    num //= 10
print(sum)
