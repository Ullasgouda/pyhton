# program is to find the length of the no.
num = int(input("Enter the no :"))
# leng = len(str(num))
# print(leng)
count = 0
while (num > 0):
    num = num//10
    count += 1
print(count)
