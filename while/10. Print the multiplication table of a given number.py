# 10. Print the multiplication table of a given number.
mul = int(input("Enter which  multiplication table you want : "))
i = 0
while i <= 10:
    print(f"{mul}X{i}={mul*i}")
    i += 1
