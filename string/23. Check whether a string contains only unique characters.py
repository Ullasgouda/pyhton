# 23. Check whether a string contains only unique characters.
str1 = input("Enter the string: ")

result = ""

for i in str1:
    if i in result:
        print("String does not contain unique characters")
        break
    else:
        result += i
else:
    print("String contains only unique characters")
