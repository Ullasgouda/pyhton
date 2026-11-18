str1 = input("Enter the string: ")

count = 1
result = ""

for i in range(len(str1)):
    if i < len(str1) - 1 and str1[i] == str1[i + 1]:
        count += 1
    else:
        result += str1[i] + str(count)
        count = 1

print(result)
