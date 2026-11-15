num = int(input("entr the number : "))
total = 0
temp = num

while (num > 0):
    rem = num % 10
    fac = 1
    i = 1
    while (i <= rem):
        fac *= i
        i += 1
    num //= 10
    total += fac
if (total == temp):
    print("is a strong no.")
else:
    print("is not a strong no")
