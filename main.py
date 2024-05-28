import os
import getpass

patth=os.path.dirname(os.path.abspath(__file__))
patth=patth+"/studentdatatherayhanpy.txt"
patth = patth.replace("\\", "/")
patth=patth[0].upper() + patth[1:]
if os.path.exists(patth) == False:
    f = open(patth,"a")
patth2=os.path.dirname(os.path.abspath(__file__))
patth2=patth2+"/adminpass.txt"
patth2 = patth2.replace("\\", "/")
patth2=patth2[0].upper() + patth2[1:]
if os.path.exists(patth2) == False:
    f = open(patth2,"a")
    with open(patth2,"w") as pas:
        pas.write("i_love_rayhan")

def admin_pass():
    benar=f'''
_____________________________________________________________________________________________________________
|                                                 Hello !!                                                  |
|                                  Plase Enter The Admin Password For confarmetion!                         |
------------------------------------------------------------------------------------------------------------- 
'''
    # big_and_bold_text = color.BOLD + play.upper() + color.END
    print(benar)
    
    
def choices():
    benar=f'''
_____________________________________________________________________________________________________________
|                                  For, Add A New Studint Data Press - ns                                   |
|                                  For, Delete A Studint Data Press - ds                                    |
|                                  For, chak A Studint Data Press - cs                                      |
|                                  To, Show All Data Have In Databass Press - adb                           |
|                                  To, Come Previous Page Press - /                                         |
------------------------------------------------------------------------------------------------------------- 
'''
    # big_and_bold_text = color.BOLD + play.upper() + color.END
    print(benar)
    

def cd_chak():
    global admin_choices
    choices()
    admin_choices=input()
    
admin_pass()
admin_chak=False
with open(patth2,"r") as adminpass:
    admin_password=getpass.getpass("Admin Password : ")
    data1=adminpass.read()
    # print(len(data1))
    if admin_password==data1[0:]:
        admin_chak=True
while True:
    if admin_chak==True:
        cd_chak()
        if admin_choices.lower() == "ns":
            while True:
                st_name=input("\nEnter The Studint Name : ")
                if st_name=="/":
                    break
                st_class=input("\nEnter The Studint Class : ")
                if st_class=="/":
                    break
                st_roll=input("\nEnter The Studint Roll : ")
                if st_roll=="/":
                    break
                with open(patth,"a") as stdata:
                    stdata.write(f"Name : {st_name} Class : {st_class} Roll : {st_roll}\n")
        elif admin_choices.lower()=="ds":
            while True:
                st_name=input("\nEnter The Studint Name : ")
                if st_name=="/":
                    break
                st_class=input("\nEnter The Studint Class : ")
                if st_class=="/":
                    break
                st_roll=input("\nEnter The Studint Roll : ")
                if st_roll=="/":
                    break
                with open(patth, "r") as stdata:
                    lines = stdata.readlines()
                with open(patth,"w") as stdata:
                    # data4=stdata.read()
                    for line in lines:
                        a=False
                        b=False
                        c=False
                        if f"Name : {st_name}" in line:
                            a=True
                        if f"Class : {st_class}" in line:
                            b=True
                        if f"Roll : {st_roll}" in line:
                            c=True
                        if a and b and c :
                            stdata.write(f"")
        elif admin_choices.lower()=="cs":
            while True:
                st_name=input("\nEnter The Studint Name : ")
                if st_name=="/":
                    break
                st_class=input("\nEnter The Studint Class : ")
                if st_class=="/":
                    break
                st_roll=input("\nEnter The Studint Roll : ")
                if st_roll=="/":
                    break
                with open(patth,"r") as stdata:
                    coc=False
                    for line in stdata:
                        a=False
                        b=False
                        c=False
                        if f"Name : {st_name}" in line:
                            a=True
                        if f"Class : {st_class}" in line:
                            b=True
                        if f"Roll : {st_roll}" in line:
                            c=True
                        if a and b and c :
                            print("\nData Already Exist\n")
                            coc=True
                    if coc==False:
                        print("\nNo Data Found\n")
        elif admin_choices.lower()=="adb":  
            with open(patth,"r") as stdata:
                # coc=False
                for line in stdata:
                    print(line)
            leve=input("Press Enter.")
        elif admin_choices=="/":
            break
        else:
            print("Ivalit choice!")
            break
            
    else:
        print("Ivalit Password!")
        break