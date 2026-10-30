a = int(input("Entre side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))
if (a+b > c) and (b+c > a) and (a+c > b):
    print(f"Triangle with sides ({a},{b},{c})is valid")
elif a == b == c:
    print("It is EQUILATERAL TRIANGLE(3 sidesare equal)")
elif a == b or b == c or c == a:
    print("It is an ISOSCELES triangle (2 sides are equal)")
else:
    print("It is a SCALENE triangle(on side are equal)")
