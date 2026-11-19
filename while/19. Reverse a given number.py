# 19. Reverse a given number.
n = int(input("number: "))
temp = []
while n > 0:
    rem = n % 10
    temp = rem
    print(temp)
    n //= 10
