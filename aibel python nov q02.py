def mobile_number_checker():
    mobile_num=str(input("enter the mobile number:"))
    if mobile_num[0]=="7"or"8"or"9":
       if len(mobile_num)==10:
        print("valid mobile number")
    else:
        print("not a valid mobile number")

mobile_number_checker()
