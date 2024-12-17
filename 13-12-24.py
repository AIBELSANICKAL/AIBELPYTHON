def monty():
    from random import randint
    choice=int(input("open a door(1,2or3:"))
    a=randint(1,4)
    if a==choice:
     secndchoice=input("open the door,revealing a car\ndo you want to mswitch your door(Y/N):")
    secndchoice.casefold()
    if secndchoice=='Y':
        finalchoice=int(input("enter your final choice:"))
        if finalchoice==a:
            print("congrats you won the car")
        else:
            print("congrats you won a goat")
    else:
        print("congrats you won a car")
    else:
    secndchoice=input("open the door,revealing a goat\ndo you want to switch your door(YorN):")
    if secndchoice=='y':
        finalchoice=int(input("enter your final choice"))
        if finalchoice==a:
            print("congrats you won the car")
        else:
            print("congrats you won the GOAT")
    else:
        print("congrats you won the goat")
monty()