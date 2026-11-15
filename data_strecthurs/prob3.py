se1 = {1000000, 220, 1212021, 212, 121212121,
       1, 232343, 34, 4, 431, 123, 123, 1212}
ls = list(se1)
med = ls[0]
ll = 0
for ele in se1:
    if ele < med:
        med = ele
    if ele > ll:
        ll = ele
print(f" {med} min")
print(f"{ll} max")
