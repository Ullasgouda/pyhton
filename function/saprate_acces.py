def cal(a, b):
    add = a+b
    sub = a-b
    mul = a+b
    div = a/b
    return add, sub, mul, div


add, sub, mul, div = cal(2, 3)
print("addition : ", add)
print("sub: ", sub)
print("multiply: ", mul)
print("devide: ", div)
