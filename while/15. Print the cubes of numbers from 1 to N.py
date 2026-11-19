# 15. Print the cubes of numbers from 1 to N.
n = int(input("ENter the number : "))
i = 1
while i <= n:
    cube = i*i*i
    i += 1
print(f"The cube of 1 to {n} is {cube}")
