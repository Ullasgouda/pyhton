name = "ullas"
v_count = 0
c_count = 0
l_count = 0
print(name[::-1])
if name == name[::-1]:
    print("polindrom")
else:
    print("not a polindrom")
for char in name:
    if char in ["a", "e", "i", "o", "u"]:
        v_count += 1
        print(f"{char} is a vowel")

    elif char not in ["a", "e", "i", "o", "u"]:
        c_count += 1
        print(f"{char} is a consonant")

else:
    print("not a alphabet")
print(f"count of vowels = {v_count}")
print(f"count of consonants = {c_count}")
ele = input("Enter the element to be searched : ")
if ele in name:
    ele_count = name.count(ele)
print(f"{ele} is present in the string")
print(f"Count of {ele} = {ele_count}")
for char in name:
    l_count += 1
print(f"Length of the string = {l_count}")
