n=int(input("enter the number:"))
sum=0
for i in range(2,n):
 if n%i==0:
     sum=sum+1
else:
    sum=sum
if sum==0:
    print("the given number is prime")
else:print("the given number is not prime")





