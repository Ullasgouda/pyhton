se1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
se2 = set()
se3 = set()
for ele in se1:
    print(ele)
    if ele % 2 == 0:
        se2.add(ele)
    else:
        se3.add(ele)
print(f"{se2} are the even numbers")
print(f"{se3} are the odd number")
