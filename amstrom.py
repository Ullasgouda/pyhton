# armstrom means for example 153 where length 3 therfore 1**3+5**3+3**3=153 where as the length is the power
num = int(input("enter your no."))
temp = num
pow = len(str(num))
c1 = 0
while (num > 0):
    r = num % 10
    c1 = c1+r**pow
    num = num//10

if (c1 == temp):
    print("armstrong")
else:
    print("not armstrong")
