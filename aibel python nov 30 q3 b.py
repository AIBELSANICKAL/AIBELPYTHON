def right_angle_triangle(side1,side2,side3):
    import math
    sides=[side1,side2,side3]
    sides.sort()
    print(sides)
    if sides[2]==math.sqrt(sides[0]**2 + sides[1]**2):
        print("the given is a right angle triangle")
    else:
        print("not a right angle triangle")

right_angle_triangle()
