def resum(name,  qualification, *skill, pass_out=None, **detail):
    print("name: ", name)
    print("pass_out: ", pass_out)
    print("qualification: ", qualification)
    print("skill :", ",".join(skill))
    for key, value in detail.items():
        print(f"{key}:{value}")


name = input("Enter the name : ")
passingyear = int(input("pass_out year: "))
degree = input("graguation (B.E OR BCA): ")
skil = int(input("how many skilles do u have: "))
skilles = []

for i in range(skil):
    skill = input("Enter skill: ")
    skilles.append(skill)
pu = float(input("what is your PU percentage : "))
sslc = float(input("what is your sslc percentage :"))
degre = float(input("what is your CGP: "))
resum(name, degree, *skilles, PUC=pu, ss=sslc, deg=degre, pass_out=passingyear)
