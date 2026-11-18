# Given the length and breadth of a rectangle, write a program to find
# whether the area of the rectangle is greater than its perimeter. For
# example, the area of the rectangle with length = 5 and breadth = 4 is
# greater than its perimeter.
length = int(input("Enter the length of the rectangle : "))
breadth = int(input("Enter the breadth of the rectangle : "))
area = length*breadth
perimeter = 2*area
if (area > perimeter):
    print("Area of the rectangel is grater then the perimeter ")
else:
    print("Ares of thr rectangle is not grater than the perimeter ")
