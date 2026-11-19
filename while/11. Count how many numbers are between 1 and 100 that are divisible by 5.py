# 11. Count how many numbers are between 1 and 100 that are divisible by 5.
count = 0
i = 1
while i <= 100:
    if i % 5 == 0:
        count += 1
        print(i)
    i += 1
print(f"There are {count} no. in between 1 to 100 divisibale by 5 ")
