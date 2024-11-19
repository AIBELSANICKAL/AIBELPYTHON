num=int(input("enter number of rows:"))
print("increasing triangle")
for i in range(num):
     for j in range(i+1):
         print("*",end=" ")
     print()

num=int(input("enter number of rows:"))
print("increasing triangle")
for i in range(num,0,1):
     for j in range(i+1):
         print("*",end=" ")
     print()