#  Write a program that takes a number (1–3) and performs:
#  1 → Addition
#  2 → Subtraction
#  3 → Multiplication
a = int(input("Enter the 1st number  : "))
b = int(input("Enter the 2nd number : "))
c = int(input("Enter the 3ed number : "))
opration = input("What opration is need to be done like(x,+,-): ").lower()
if (opration == 'x'):
    mul = a*b*c
    print(f"multiplication of 1st,2nd,3ed number is {mul}")
elif (opration == '+'):
    add = a+b+c
    print(f"Addition of 1st,2nd,3ed number is {add} ")
elif (opration == "-"):
    sub = a-b-c
    print(f"Subtraction of 1st,2nd,3ed number is {sub} ")
else:
    print("You had enter in valid opration ")
