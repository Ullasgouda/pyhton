# 25. Insert one string into the middle of another string.
strint = input("Enter the string: ")
leng = len(strint)
mid = leng//2
result = ""

result += strint[0:mid]
result += input("Enter the senter word : ")
result += strint[mid:leng]
print(result)
