tempurature=float(input("enter the tempurature:"))
unit=input("is the tempurature is fahrenheit or celsius(c or f:")
if unit=="c" or unit=="C":
    faran=(9/5*tempurature)+32
    print(faran,"f")
elif unit=="f" or unit=="F":
    cels=5/9*(tempurature-32)
    print(cels,"c")
