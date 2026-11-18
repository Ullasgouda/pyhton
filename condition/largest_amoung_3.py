# Write a program to find the largest of three numbers.
a = int(input("Enter the value of the a"))
b = int(input("Enter the value of the b"))
c = int(input("Enter the value of the c"))
if (a > b and a > c):
    print(f"a={a} is grater the {b} and {c}")
elif (b > a and b > c):
    print(f"b={b} id grater then {a} and {c}")
elif (c > a and c > b):
    print(f"c={c} is grater that {a} and {b}")
else:
    print(f"{a} {b} {c} are same")
