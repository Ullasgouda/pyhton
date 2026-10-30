# program is to find the length of the no.
num = int(input("Enter the no :"))
count = 0
while (num > 0):
    num = num//10
    count += 1
print(count)
