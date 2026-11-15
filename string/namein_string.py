name = "Python"
print(id(name))
name = "Java"
print(id(name))
print(name)
a = "python"
b = "python"
print(id(a))
print(id(b))
print(a is b)
a = "Python"
b = 1234
print(hash(a))
print(hash(b))
# dic = {"name":"pradeep", "no": 8998}
# print(hash(dic))
tup = [5, 8, 9, 8]
print(hash(tup))
list = []
