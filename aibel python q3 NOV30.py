def right_angle_triangle():
    side1=int(input("enter the length of the first side:"))
    side2=int(input("enter the length of the second side:"))
    side3=int(input("enter the length of the third side:"))
    dimensions=[side1,side2,side3]
    dimensions.sort()
    if dimensions[-1]**2==(dimensions[-2]**2 + dimensions[-3]**2):
        print("given triangle is a right angled triangle")
    else:
        print("not a right angled triangle")

right_angle_triangle()

