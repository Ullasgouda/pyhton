student = 0


def student_detail(**detail):
    global student
    student += 1
    print(f"student{student} details: ")
    for key, value in detail.items():
        print(f"{key}:{value}")


no_of_stu = int(input("enter the no of students"))
for i in range(0, no_of_stu):
    name1 = input("Enter the name : ")
    marks1 = int(input("Enter the marks: "))
    place1 = input("Enter where he is from : ")
    student_detail(name=name1, marks=marks1, place=place1)
