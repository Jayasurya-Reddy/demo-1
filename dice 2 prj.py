def register():
    pname=input("username :")

    with open("users.txt ","r") as x :
        data=x.readlines()
    print(data)
    users=[ i.split(",") [0] for i in data ]
    print(users)


    while True :
        if pname not in users :
            pwd=input("Password :")
            phno=int(input("Phone number :"))
            rec=pname+","+pwd+","+str(phno)+"\n"
            with open ("users .txt","a") as x :
                x.write(rec )
            print("you registered successfully .")
            break
        else :
            print("user already exist")
            pname=input("enter different username :")

def is_valid_player(p1_name,users) :
     while True:
         if p1_name in users :
             print("welcome ",p1_name,"to play the game ")
             break
         else :
            print("Invalid player name")
            p1_name=input("enter player name :")
def login() :
    with open("users.txt","r") as x:
         data=x.readlines()
    users=[ i.split (",") [0] for i in]
    p11=input("enter player name 1 :")

    is_valid_player(p11,users)
    p12=input("enter player name 2 :")
    is_valid_player(p12,users)

def menu() :
    print("_" * 80)
    print("\t\t\t welcome to play dice game # tecnosoft station")
    print("_" * 80)

    print("\t\t\t Main Menu")
    print("\t\t 1. Login")
    print("\t\t 2.register")
    print("\t\t 3.Exit")
    ans=int(input("enter choice :"))
    if ans==1:
        login()
    elif ans==2:
        register()
        time.sleep(2)
        menu()
    elif ans==3 :
        print("Thank you ,Have a Great day!!!")
        ays.exit(0)
import time,sys
if __name__=="__main__" :
    menu()
    





    
    







    
