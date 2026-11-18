sent = input("Enter the entensce: ")
result = ""
for i in sent.split():
    result += i[::-1]+" "
print(result)
