ls = ["pradeep", "ullas", 123.1, 111, True, False, 1, 0, 111, 2+3j]
st1 = set(ls)
count = 0
for ele in st1:
    count += 1
print(f"no of elements are {count} ")
print("*"*100)
unique = []
for item in st1:
    unique.append(item)
count1 = 0
for ele in unique:
    count1 += 1
print(count1)
print("*"*100)
lls = len(ls)
lst1 = len(st1)
length = lls-lst1
print(length)
