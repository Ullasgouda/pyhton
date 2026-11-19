# 13. Find the average of numbers from 1 to N.
n = int(input("Enter the number : "))
i = 1
sum = 0
while i <= n:
    sum += i
    avg = sum/n

    i += 1
print(sum)
print(f"average : {avg}")
