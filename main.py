import os
import getpass
from termcolor import colored

class Rcolor():
    def background(code):
        return "\33[{code}m".format(code=code)
 
    def style_text(code):
        return "\33[{code}m".format(code=code)
 
    def color_text(code):
        return "\33[{code}m".format(code=code)

patth = os.path.dirname(os.path.abspath(__file__))
patth = patth + "/studentdatatherayhanpy.txt"
patth = patth.replace("\\", "/")
patth = patth[0].upper() + patth[1:]
if not os.path.exists(patth):
    f = open(patth, "a")
patth2 = os.path.dirname(os.path.abspath(__file__))
patth2 = patth2 + "/adminpass.txt"
patth2 = patth2.replace("\\", "/")
patth2 = patth2[0].upper() + patth2[1:]
if not os.path.exists(patth2):
    f = open(patth2, "a")
    with open(patth2, "w") as pas:
        xw = ""
        for mm in "i_love_rayhan":
            xw = xw + format(ord(mm), "b")
        pas.write(xw)

def admin_pass():
    benar = colored('''
_____________________________________________________________________________________________________________
|                                                 Hello !!                                                  |
|                                  Please Enter The Admin Password For confirmation!                         |
-------------------------------------------------------------------------------------------------------------
''', "blue")
    print(benar)
    
def choices():
    benar = colored('''
_____________________________________________________________________________________________________________
|                                  For, Add A New Student Data Press - ns                                   |
|                                  For, Delete A Student Data Press - ds                                    |
|                                  For, Check A Student Data Press - cs                                     |
|                                  For, Update A Student Data Press - us                                    |
|                                  To, Show All Data in Database Press - adb                                |
|                                  To, Change Admin Password Press - ac                                     |
|                                  To, Come Previous Page Press - /                                         |
-------------------------------------------------------------------------------------------------------------
''', "blue")
    print(benar)
    
def cd_chak():
    global admin_choices
    choices()
    admin_choices = input("Enter your choice: ")

admin_pass()
admin_chak = False
with open(patth2, "r") as adminpass:
    data1 = adminpass.read()
    admin_password = getpass.getpass("Admin Password: ")
    S_password = "".join(format(ord(c), "b") for c in admin_password)
    if str(data1) == str(S_password):
        admin_chak = True

while True:
    if admin_chak:
        cd_chak()
        if admin_choices.lower() == "us":
            while True:
                st_name = input("\nEnter The Student Name: ")
                if st_name == "/":
                    break
                st_class = input("\nEnter The Student Class: ")
                if st_class == "/":
                    break
                st_roll = input("\nEnter The Student Roll: ")
                if st_roll == "/":
                    break
                
                with open(patth, "r") as stdata:
                    lines = stdata.readlines()
                with open(patth, "a") as stdata:
                    print(lines)
                    for w in range(len(lines)):
                        if st_name in lines[w] and st_class in lines[w] and st_roll in lines[w]:
                            st_name1 = input("\nEnter The Student New Name: ")
                            if st_name1 == "/":
                                break
                            st_class1 = input("\nEnter The Student New Class: ")
                            if st_class1 == "/":
                                break
                            st_roll1 = input("\nEnter The Student New Roll: ")
                            if st_roll1 == "/":
                                break
                            lines[w] = f"Name: {st_name1} Class: {st_class1} Roll: {st_roll1}\n"
                with open(patth, "w") as stdata:
                    stdata.write("")
                    stdata.writelines(lines)
                    
        elif admin_choices.lower() == "ac":
            admin_password = getpass.getpass("Enter New Admin Password: ")
            with open(patth2, "w") as pas:
                xw = ""
                for mm in admin_password:
                    xw = xw + format(ord(mm), "b")
                pas.write(xw)
            input("Press Enter.")
            
        elif admin_choices.lower() == "ns":
            while True:
                st_name = input("\nEnter The Student Name: ")
                if st_name == "/":
                    break
                st_class = input("\nEnter The Student Class: ")
                if st_class == "/":
                    break
                st_roll = input("\nEnter The Student Roll: ")
                if st_roll == "/":
                    break
                with open(patth, "a") as stdata:
                    stdata.write(f"Name: {st_name} Class: {st_class} Roll: {st_roll}\n")
                    
        elif admin_choices.lower() == "ds":
            while True:
                st_name = input("\nEnter The Student Name: ")
                if st_name == "/":
                    break
                st_class = input("\nEnter The Student Class: ")
                if st_class == "/":
                    break
                st_roll = input("\nEnter The Student Roll: ")
                if st_roll == "/":
                    break
                with open(patth, "r") as stdata:
                    lines = stdata.readlines()
                with open(patth, "w") as stdata:
                    for qq in range(len(lines)):
                        a, b, c = False, False, False
                        if f"Name: {st_name}" in lines[qq]:
                            a = True
                        if f"Class: {st_class}" in lines[qq]:
                            b = True
                        if f"Roll: {st_roll}" in lines[qq]:
                            c = True
                        if a and b and c:
                            print(f"Are You sure? You Want To Delete - Name: {st_name} Class: {st_class} Roll: {st_roll} Data?")
                            com = input("yes - y and no - n: ")
                            if com.lower() == "y":
                                lines[qq] = ""
                                with open(patth, "w") as stdata:
                                    stdata.writelines(lines)
                                print("Data Deleted!")
                            elif com.lower() == "n":
                                stdata.writelines(lines)
                                print("Data Is Not Deleted.")
                            else:
                                stdata.writelines(lines)
                                print("Invalid Command!")
                                
        elif admin_choices.lower() == "cs":
            while True:
                st_name = input("\nEnter The Student Name: ")
                if st_name == "/":
                    break
                st_class = input("\nEnter The Student Class: ")
                if st_class == "/":
                    break
                st_roll = input("\nEnter The Student Roll: ")
                if st_roll == "/":
                    break
                with open(patth, "r") as stdata:
                    coc = False
                    for line in stdata:
                        a, b, c = False, False, False
                        if f"Name: {st_name}" in line:
                            a = True
                        if f"Class: {st_class}" in line:
                            b = True
                        if f"Roll: {st_roll}" in line:
                            c = True
                        if a and b and c:
                            print("\nData Already Exists\n")
                            coc = True
                            break
                    if not coc:
                        print("\nNo Data Found\n")
                        
        elif admin_choices.lower() == "adb":  
            with open(patth, "r") as stdata:
                for line in stdata:
                    print(line)
            input("Press Enter.")
            
        elif admin_choices == "/":
            break
        else:
            print("Invalid choice!")
            
    else:
        print("Invalid Password!")
        break

