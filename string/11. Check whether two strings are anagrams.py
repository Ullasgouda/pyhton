st1 = input("Enter the string 1: ").lower()
st2 = input("Enter the string 2: ").lower()
if (len(st1) == len(st2)):
    for i in st1:
        if st1.count(i) == st2.count(i):
            print("its anagrams(length)")
            break

    else:
        print("its  not anagrams ")
else:
    print("It's not an anagram")
