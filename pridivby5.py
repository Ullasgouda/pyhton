# printing no.divesibal by 5
num = int(input("Enter the no. till where u want the 5 div: "))
i = 0
while (i <= num):
    if (i % 5 == 0):
        print(i)
    i += 1
else:
    print("loap")
