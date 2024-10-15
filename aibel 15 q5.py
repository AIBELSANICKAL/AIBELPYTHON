number=int(input("enter the the number"))

 sum=0

 while (number>0):
     remainder=number%10
     number=number//10
     sum=sum+remainder
 print(sum)