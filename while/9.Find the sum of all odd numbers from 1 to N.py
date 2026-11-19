# Find the sum of all odd numbers from 1 to N.
n = int(input("Enter the number : "))
temp = 0
i = 1
while i <= n:
    if i % 2 != 0:
        temp += i
    i += 1
print(temp)
