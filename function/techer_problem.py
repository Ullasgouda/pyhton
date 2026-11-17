# """
# A teacher wants to calculate the total and average marks of a student. Different students may have different numbers of subjects.

# Task:
# - Create a function student_result(*marks).
# - Accept marks of any number of subjects.
# - Display total marks and average marks.
# - Display the highest and lowest marks.
# """
def student_result(*marks):
    total = sum(marks)
    avg = total/len(marks)
    max = max(marks)
    min = min(marks)
    print(f"Total:{total}")
    print(f"avrage:{avg}")
    print(f"maximum:{max}")
    print(f"minimum:{min}")


student_result(10, 20, 30, 40, 50)
student_result(10, 20, 30, 40, 50, 60)
student_result(10, 20, 30, 40, 50, 70, 60)
student_result(10, 20, 30, 40, 50, 59, 50, 10)
student_result(10, 20, 30, 40, 50, 30, 30, 30, 30)
student_result(10, 20, 30, 40, 50, 80, 90, 90, 90, 90)
