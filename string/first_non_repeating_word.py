name = input("Enter the name : ")
for ele in name:
    count = 0
    for i in name:
        if ele == i:
            count += 1
    if count == 1:
        print(f"{ele} is the first wlement to not reapeet ")
        break
