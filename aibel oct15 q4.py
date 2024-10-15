''''

name aibel s anickal
 date 15-10-22024
 version 1:0
 ''

purchase_amount=int(input("purchase amount:"))
if purchase_amount>500:
   final_amount=purchase_amount*0.8
   print(final_amount)
elif purchase_amount>=200 and purchase_amount<=500:
     discount=purchase_amount*0.9
     print(discount)
else:
    print('no discount applied')
