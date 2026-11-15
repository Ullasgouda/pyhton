def cal_add():
    global c
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    c = a + b

    return f"{a}+{b}={c}"


a = cal_add()
print(c)
