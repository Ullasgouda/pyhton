# 18. Check whether one string is a rotation of another.
word1 = input("Enter the word1 : ")
word2 = input("Enter the word2 : ")
if len(word1) == len(word2) and word2 in word1+word1:
    print("one string is a rotation of another.")
else:
    print("not rotating od one another")
