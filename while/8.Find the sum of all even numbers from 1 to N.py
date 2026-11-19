# Find the sum of all even numbers from 1 to N.
n = int(input("Enter the number : "))
temp = 0
i = 1
while i <= n:
    if (i % 2 == 0):
        # print(i)
        # print("*"*100)
        temp += i
        # print(temp)
        # print("*"*100)
    i += 1
print(temp)
