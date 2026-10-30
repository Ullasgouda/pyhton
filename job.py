edu = input("Are you graduated(yes or no): ").lower()
lan = input("which language you know (Python , Java , C++ ,C): ").lower()
exp = int(input("How many year experience: "))
cutoff = float(input("Your cgpa(in points )"))
if (edu == 'yes'):
    if (lan == 'python' or lan == 'java' or lan == 'c++' or lan == 'c'):
        if (exp >= 8):
            if (cutoff >= 9.5):
                print("Eligible")
else:
    print("Not Eligible")
