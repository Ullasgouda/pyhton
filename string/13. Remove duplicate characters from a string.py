
sent = input("Enter any sentence: ")

result = ""

for i in sent.lower().replace(",", "").replace(".", "").split():
    if i not in result.split():
        result += i + " "

print("Original sentence:", sent)
print("*" * 100)
print("After removing duplicate words:", result.strip())
