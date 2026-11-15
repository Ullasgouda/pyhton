name = input("Enter yoyr name ")
i = [0]
for ele in str(name):
    count1 = 0
    for i in name:
        if i == ele:
            count1 += 1
    print(f"{ele} repeted for {count1} times")
