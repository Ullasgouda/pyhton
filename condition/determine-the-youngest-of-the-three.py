Ram = int(input("Enter the age of Ram : "))
Shyam = int(input("Enter the age of Shyam : "))
Ajay = int(input("enter the age of Ajay"))
if (Ram > Shyam and Ram > Ajay):
    print("Ram is elder")
elif (Shyam > Ram and Shyam > Ajay):
    print("Shyam is elder ")
else:
    print("Ajay is elder")
