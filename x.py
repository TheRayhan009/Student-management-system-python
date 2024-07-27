import os
import getpass
# from termcolor import colored

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

patth3 = os.path.dirname(os.path.abspath(__file__))
patth3 = patth3 + "/attensence.txt"
patth3 = patth3.replace("\\", "/")
patth3 = patth3[0].upper() + patth3[1:]
if not os.path.exists(patth3):
    f = open(patth3, "a")

patth4 = os.path.dirname(os.path.abspath(__file__))
patth4 = patth4 + "/teachersdata.txt"
patth4 = patth4.replace("\\", "/")
patth4 = patth4[0].upper() + patth4[1:]
if not os.path.exists(patth4):
    f = open(patth4, "a")
    

patth5 = os.path.dirname(os.path.abspath(__file__))
patth5 = patth5 + "/homework.txt"
patth5 = patth5.replace("\\", "/")
patth5 = patth5[0].upper() + patth5[1:]
if not os.path.exists(patth5):
    f = open(patth5, "a")

def s_or_a():
    global admin_or_student_chak
    sora = '''
_____________________________________________________________________________________________________________
|                                                 Hello !!                                                  |
|                                                                                                           |
|                                    If You Are a Student Then Press - 1                                    |
|                                     If You Are a Admin Then Press - 2                                     |
|                                    If You Are a Teacher Then Press - 3                                    |
|                                     To, Come Previous Page Press - /                                      |
-------------------------------------------------------------------------------------------------------------
'''
    print(sora)
    
def admin_pass():
    benar = '''
_____________________________________________________________________________________________________________
|                                                 Hello !!                                                  |
|                                  Please Enter The Admin Password For Confirmation!                        |
-------------------------------------------------------------------------------------------------------------
'''
    print(benar)
    
    
def teacher_chak():
    benar = '''
_____________________________________________________________________________________________________________
|                                            Hello !! Teacher !!                                            |
|                                Please Enter The Your Impormation For Confirmation!                        |
-------------------------------------------------------------------------------------------------------------
'''
    print(benar)
    

def teacher_panel(T_name1):
    faw_space=44-len(T_name1)
    faw_space*=" "
    benar = f'''
_____________________________________________________________________________________________________________
|                                            Hello !! {T_name1} !!       {faw_space}|
|                                       For, Upload A Homework press -hw                                    |
|                                       For, Edit A Homework press -ew                                      |
|                                       To, Come Previous Page Press - /                                    |
-------------------------------------------------------------------------------------------------------------
'''
    print(benar)

    
def date_skip():
    benar = '''
_____________________________________________________________________________________________________________
|                                                 Hello !!                                                  |
|                                    For Skip Date Option Type - ( 0/0/0 )                                  |
-------------------------------------------------------------------------------------------------------------
'''
    print(benar)
    
def choices():
    benar = '''
_____________________________________________________________________________________________________________
|                                  For, Add A New Student Data Press - ns                                   |
|                                  For, Delete A Student Data Press - ds                                    |
|                                  For, Check A Student Data Press - cs                                     |
|                                  For, Update A Student Data Press - us                                    |
|                                  To, Show All Data in Database Press - asd                                |
|                                  To, Show specepic Class Student Data Press - spc                         |
|                                  To, Show specepic Day Student Attendence Data Press - spa                |
|                                  To, See All Teachers Data Press - allt                                   |
|                                  To, Add Teachers Data Press - atd                                        |
|                                  To, Edit Teachers Data Press - etd                                       |
|                                  To, Reset All Homework press - rw                                        |
|                                  To, Change Admin Password Press - ac                                     |
|                                  To, Come Previous Page Press - /                                         |
-------------------------------------------------------------------------------------------------------------
'''
    print(benar)
    
def choices2s():
    benar = '''
_____________________________________________________________________________________________________________
|                                       For, Attendence Press - at                                           |
|                                  To, See Todays Homework Press - sh                                        |
|                                For, End The Attendence Qure Enter - exit()                                 |      
|                                  To, Come Previous Page Press - /                                          |
-------------------------------------------------------------------------------------------------------------
'''
    print(benar)

def mainx(admin_or_student_chak):
    global chhhak
    if admin_or_student_chak == "1":
        while True:
            choices2s()
            s_choice=input("Enter Your Choice: ")
            if s_choice=="at":
                dd,mm,yy=map(int,input("dd/mm/yy : ").split("/"))
                with open(patth3, "a") as atan:
                    atan.write(f"Date: {dd}/{mm}/{yy}\n")
                    while True:
                        st_name = input("\nEnter The Student Name: ")
                        if st_name == "exit()":
                            break
                        st_class = input("\nEnter The Student Class: ")
                        if st_class == "exit()":
                            break
                        st_roll = input("\nEnter The Student Roll: ")
                        if st_roll == "exit()":
                            break
                        st_sec = input("\nEnter The Student Section: ")
                        if st_sec == "exit()":
                            break
                        atan.write(f"Name: {st_name} Class: {st_class} Roll: {st_roll} Section: {st_sec}\n")
            elif s_choice=="sh":
                class_s=input("\nEnter Class: ")
                class_sec=input("\nEnter Scetion: ")
                class_sub=input("\nEnter Subject: ")
                with open(patth5,"r") as hw:
                    line=hw.readlines()
                for i in range(0,len(line)):
                    a,b,c=False,False,False
                    chakk=False
                    if f"Class: {class_s}" in line[i] and class_s != "":
                        a=True
                    if f"Section: {class_sec}" in line[i] and class_sec != "":
                        b=True
                    if f"Subject: {class_sub}" in line[i] and class_sub != "":
                        c=True
                    if a and b and c:
                        chakk=True
                        x=line[i].find("Homework:")
                        # print(x)
                        print("\n"+line[i][x+10:])
                        input("This Is Your Homework. Press Enter.")
                        break
                if chakk==False:
                    print("\nNo Data Have..!")
            elif s_choice=="/":
                break
            else:
                print("Invalid choice!")
            


    elif admin_or_student_chak =="2":
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
                        st_sec = input("\nEnter The Student Section: ")
                        if st_sec == "/":
                            break
                        with open(patth, "r") as stdata:
                            lines = stdata.readlines()
                        with open(patth, "a") as stdata:
                            for w in range(len(lines)):
                                if st_name in lines[w] and st_class in lines[w] and st_roll in lines[w] and st_sec in lines[w]:
                                    st_name1 = input("\nEnter The Student New Name: ")
                                    if st_name1 == "/":
                                        break
                                    st_class1 = input("\nEnter The Student New Class: ")
                                    if st_class1 == "/":
                                        break
                                    st_roll1 = input("\nEnter The Student New Roll: ")
                                    if st_roll1 == "/":
                                        break
                                    st_sec = input("\nEnter The Student Section: ")
                                    if st_sec == "/":
                                        break
                                    lines[w] = f"Name: {st_name1} Class: {st_class1} Roll: {st_roll1} Section: {st_sec}\n"
                        with open(patth, "w") as stdata:
                            stdata.write("")
                            stdata.writelines(lines)
                
                elif admin_choices.lower() == "rw":
                    with open(patth5,"w") as rw:
                        rw.write("")
                    input("Homework Is Reseted. Press Enter..")
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
                        st_sec = input("\nEnter The Student Section: ")
                        if st_sec == "/":
                            break
                        with open(patth, "a") as stdata:
                            stdata.write(f"Name: {st_name} Class: {st_class} Roll: {st_roll} Section: {st_sec}\n")
                            
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
                        st_sec = input("\nEnter The Student Section: ")
                        if st_sec == "/":
                            break
                        with open(patth, "r") as stdata:
                            lines = stdata.readlines()
                        with open(patth, "w") as stdata:
                            for qq in range(len(lines)):
                                a , b , c , d= False, False, False, False
                                if f"Name: {st_name}" in lines[qq]:
                                    a = True
                                if f"Class: {st_class}" in lines[qq]:
                                    b = True
                                if f"Roll: {st_roll}" in lines[qq]:
                                    c = True
                                if f"Section: {st_sec}" in lines[qq]:
                                    d = True
                                
                                if a and b and c and d:
                                    print(f"Are You sure? You Want To Delete - Name: {st_name} Class: {st_class} Roll: {st_roll} Section: {st_sec} Data?")
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
                        st_sec = input("\nEnter The Student Section: ")
                        if st_sec == "/":
                            break
                        with open(patth, "r") as stdata:
                            coc = True
                            for line in stdata:
                                a, b, c, d = False, False, False, False
                                if f"Name: {st_name}" in line:
                                    a = True
                                if f"Class: {st_class}" in line:
                                    b = True
                                if f"Roll: {st_roll}" in line:
                                    c = True
                                if f"Section: {st_sec}" in lines[qq]:
                                    d = True
                                if a and b and c and d:
                                    print("\nData Already Exists\n")
                                    coc = False
                                    break
                            if coc:
                                print("\nNo Data Found\n")
                elif admin_choices.lower() == "spc":
                    st_class = input("\nEnter The Student Class: ")
                    if st_class == "/":
                        break
                    st_sec = input("\nEnter The Student Section: ")
                    if st_sec == "/":
                        break
                    with open(patth, "r") as stdata:
                        for line in stdata:
                            b,d = False, False
                            if f"Class: {st_class}" in line:
                                b = True
                            if f"Section: {st_sec}" in line:
                                d = True
                            if b and d:
                                print("\n",line)   
                        input("Press Enter.")      
                
                elif admin_choices.lower() == "atd":
                    while True:
                        T_name = input("\nEnter Name: ")
                        if T_name=="/":
                            break
                        T_sub = input("\nEnter Subject: ")
                        if T_sub=="/":
                            break
                        T_pass = "12345678"
                        input("\nTeacher Primary Password is \" 12345678 \" \n")
                        b_code=""
                        for k in range(0,len(T_pass)):
                            b_code = b_code + format(ord(T_pass[k]),"b")
                        T_pass=b_code
                        with open(patth4,"a") as t:
                            t.write(f"Name: {T_name} Subject: {T_sub} Password: {T_pass}\n")
                
                elif admin_choices.lower() == "etd":
                    while True:
                        S_key_chak=False
                        T_name1 = input("\nEnter Name: ")
                        if T_name1=="/":
                            break
                        T_sub1 = input("\nEnter Subject: ")
                        if T_sub1=="/":
                            break
                        T_pass1 = input("\nEnter Spacial Key or Enter Password: ")
                        if T_pass1=="/":
                            break
                        if T_pass1=="FCHS":
                            S_key_chak=True
                            
                        b_code=""
                        for k in range(0,len(T_pass1)):
                            b_code = b_code + format(ord(T_pass1[k]),"b")
                        T_pass1=b_code
                       
                        with open(patth4,"r") as t:
                            line=t.readlines()
                        with open(patth4,"a") as t:
                            if S_key_chak==True:
                                for i in range(0,len(line)):
                                    a,b=False,False
                                    chhhak=False
                                    if f"Name: {T_name1}" in line[i] and T_name1 != "":
                                        a=True
                                    if f"Subject: {T_sub1}" in line[i] and T_sub1 != "":
                                        b=True
                                    if a and b:
                                        chhhak=True
                                        T_name = input("\nEnter The New Name: ")
                                        if T_name=="/":
                                            break
                                        T_sub = input("\nEnter The New Subject: ")
                                        if T_sub=="/":
                                            break
                                        T_pass = input("\nEnter The New Password: ")
                                        if T_pass=="/":
                                            break
                                        b_code=""
                                        for k in range(0,len(T_pass)):
                                            b_code = b_code + format(ord(T_pass[k]),"b")
                                        T_pass=b_code
                                        line[i]=f"Name: {T_name} Subject: {T_sub} Password: {T_pass}\n"
                                if chhhak==False:
                                    print("\nOpps!! No Data Hve!")
                                with open(patth4, "w") as t:
                                    t.write("")
                                    t.writelines(line)
                            else:
                                for i in range(0,len(line)):
                                    a,b,c=False,False,False
                                    chhhak=False
                                    if f"Name: {T_name1}" in line[i] and T_name1 != "":
                                        a=True
                                    if f"Subject: {T_sub1}" in line[i] and T_sub1 != "":
                                        b=True
                                    if f"Password: {T_pass1}" in line[i] and T_pass1 != "":
                                        c=True
                                    # print(a,b,c)
                                    if a and b and c:
                                        chhhak=True
                                        T_name = input("\nEnter The New Name: ")
                                        if T_name=="/":
                                            break
                                        T_sub = input("\nEnter The New Subject: ")
                                        if T_sub=="/":
                                            break
                                        T_pass = input("\nEnter The New Password: ")
                                        if T_pass=="/":
                                            break
                                        b_code=""
                                        for k in range(0,len(T_pass)):
                                            b_code = b_code + format(ord(T_pass[k]),"b")
                                        T_pass=b_code
                                        line[i]=f"Name: {T_name} Subject: {T_sub} Password: {T_pass}\n"
                                if chhhak==False:
                                    print("\nOpps!! No Data Hve!")
                                with open(patth4, "w") as t:
                                    t.write("")
                                    t.writelines(line)
                
                elif admin_choices.lower() == "spa":
                    date_skip()
                    dd,mm,yy=map(str,input("dd/mm/yy : ").split("/"))
                    if dd+"/"+mm+"/"+yy=="0/0/0":
                        print("\nSkiped !!\n")
                    else:
                        with open(patth3, "r") as stdata:
                            lines = stdata.readlines()
                        xx=0
                        have_chak=True
                        for i in range(0,len(lines)):
                            if "Date: "+str(dd)+"/"+str(mm)+"/"+str(yy)+"\n"==lines[i]:
                                have_chak=False
                                for z in range(i,len(lines)):
                                    if "Date: " in lines[z] and xx!=0:
                                        break
                                    else:
                                        xx+=1
                                    print("\n"+lines[z])
                        if have_chak==True:
                            print("\nOpps !! No Data Have!.\n")
                    input("Press Enter.")       
                        
                elif admin_choices.lower() == "asd":  
                    with open(patth, "r") as stdata:
                        for line in stdata:
                            print(line)
                    input("Press Enter.")
                
                elif admin_choices.lower() == "allt":  
                    with open(patth4, "r") as th:
                        for line in th:
                            print(line)
                    input("Press Enter.")
                
                elif admin_choices == "/":
                    break
                else:
                    print("Invalid choice!")
                    
            else:
                print("Invalid Password!")
                break
    elif admin_or_student_chak=="3":
        while True:
            teacher_chak()
            T_name = input("\nEnter Your Name: ")
            if T_name=="/":
                break
            T_sub = input("\nEnter Your Subject: ")
            if T_sub=="/":
                break
            T_pass = getpass.getpass("\nEnter Your Password: ")
            if T_pass=="/":
                break
            b_code=""
            for k in range(0,len(T_pass)):
                b_code = b_code + format(ord(T_pass[k]),"b")
            T_pass=b_code
            with open(patth4,"r") as td:
                line=td.readlines()
                for i in range(0,len(line)):
                    a,b,c=False,False,False
                    chhhak=False
                    if f"Name: {T_name}" in line[i] and T_name != "":
                        a=True
                    if f"Subject: {T_sub}" in line[i] and T_sub != "":
                        b=True
                    if f"Password: {T_pass}" in line[i] and T_pass != "":
                        c=True
                    if a and b and c:
                        chhhak=True
                        break
            if chhhak==True:
                teacher_panel(T_name)
                T_choice=input("\nEnter Your Choice: ")
                if T_choice.lower()=="hw":
                    while True:
                        class_s=input("\nEnter Class: ")
                        if class_s =="/":
                            break
                        class_sec=input("\nEnter Scetion: ")
                        if class_sec =="/":
                            break
                        class_sub=input("\nEnter Subject: ")
                        if class_sub =="/":
                            break
                        class_homework=input("\nEnter Your Homework: ")
                        if class_homework =="/":
                            break
                        with open(patth5,"a") as hww:
                            hww.write(f"Class: {class_s} Section: {class_sec} Subject: {class_sub} Homework: {class_homework}\n")
                        input("Homework Uploaded!! Press Enter.")
                elif T_choice=="ew":
                    while True:
                        class_s=input("\nEnter Class: ")
                        if class_s =="/":
                            break
                        class_sec=input("\nEnter Scetion: ")
                        if class_sec =="/":
                            break
                        class_sub=input("\nEnter Subject: ")
                        if class_sub =="/":
                            break
                        with open(patth5,"r") as ew:
                            lines=ew.readlines()
                        for i in range(0,len(lines)):
                            a,b,c=False,False,False
                            chhhak=False
                            if f"Class: {class_s}" in lines[i] and class_s != "":
                                a=True
                            if f"Section: {class_sec}" in lines[i] and class_sec != "":
                                b=True
                            if f"Subject: {class_sub}" in lines[i] and class_sub != "":
                                c=True
                            if a and b and c:
                                chhhak=True
                                new_homework=input("\nEnter Your New Homework: ")
                                lines[i]=f"Class: {class_s} Section: {class_sec} Subject: {class_sub} Homework: {new_homework}\n"
                                with open(patth5,"w") as ew:
                                    ew.write("")
                                    ew.writelines(lines)
                        if chhhak==False:
                            print("\nOpps!! No Data Have!!.")
                else:
                    print("Invalid choice!")
            else:
                input("\nWrong Impormetion..")
    else:
        print("Invalid choice!")

while True:
    s_or_a()
    admin_or_student_chak=input("--> ")
    if admin_or_student_chak=="/":
        break
    mainx(admin_or_student_chak)
    
# The End..