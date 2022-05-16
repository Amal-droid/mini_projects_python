name = input("what is your name?  ")
print("welcome",name,"to this Adventure")
answer = input("you are on a road which way you want to go, left or right?   ").lower()

if answer == "left":
    answer = input("you come to a river,you wanna a,walk around or b,swim the river!!!   ")
    if answer == "a":
        print("walk and survive to village")
    elif answer == "b":
        print("if you swim,and were eaten by an aligator ")


elif answer == "right":
    answer = input("you comme to a bridge, wanna cross or go back")
    if answer == "back":
        print("lets back to the lost road")
    elif answer == "cross":
        answer =input("lets find adventures accross the bridge, if find a stranger do you talk to them").lower()
        if answer == "yes":
            print("level up")
        elif answer == "no":
            print("lets move")  
else:
    print("not a valid option you loose")    