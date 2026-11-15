num = int(input("Enter the range u want : "))
for i in range(0, 100, 1):
    if (i % num == 0):
        print(i)
else:
    print("Done")
