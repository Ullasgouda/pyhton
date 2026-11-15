num = int(input("Enter a number: "))
temp = num
sum = 0
i = len(str(num))
for i in range(1, i+1, 1):
    if (temp > 0):
        rem = temp % 10
        sum += rem
        temp = temp//10
print(f"Sum = {sum}")
