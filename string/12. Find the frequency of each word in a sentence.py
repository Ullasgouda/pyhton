
sent = input("write any sentence")
word = input(
    "Enter the word u want to chuck the how many times its in the sentence : ")

ls = sent.split()
count = 0
for i in ls:
    if i == word:
        count += 1
print(f"The word has frequency {count} times")
