import os
import time
from tkinter import *

def btn_scws():
    print ("btn_scws")
    os.startfile('SCWS.py')
def btn_scwt():
    print ("btn_scwt")
    os.startfile('SCWT.py')
    
def Look():
    print("Look")
def Restart():
    print("Restart")
def Sleep():
    print("Sleep")
def Change_your_account_name():
    print("Change_your_account_name")
def Change_your_account_password():
    print("Change_your_account_password")
def Change_your_account_IP():
    print("Change_your_account_IP")
def Change_your_SERVER():
    print("Change_your_SERVER")
    
def About_System():
    print("About_System")
    os.startfile('about.py')
def System_Help():
    print("System_Help")
def Application_Help():
    print("Application_Help")
def Software_Help():
    print("Software_Help")
    
sc = Tk()

fileicon = PhotoImage(file='../Pictures/smartcontrol.png')
sc.tk.call('wm', 'iconphoto', sc._w, fileicon)

screen_width = sc.winfo_screenwidth()
screen_height = sc.winfo_screenheight()
btnsizeh = int(screen_height/15)
btnsizew = int(screen_height/8.5)

sc.geometry("%sx%s+0+0"%(screen_width,screen_height))
sc.resizable(width=True, height=True)

sc.title("Smart Home System Software V 1.0.0 - Smart Control")

menubar = Menu(sc)

filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label = "Look", command = Look)
filemenu.add_command(label = "Restart", command = Restart)
filemenu.add_command(label = "Sleep", command = Sleep)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = sc.quit)
menubar.add_cascade(label = "File", menu = filemenu)

edit = Menu(menubar, tearoff = 0)
edit.add_command(label = "Change your account name", command = Change_your_account_name)
edit.add_command(label = "Change your account password", command = Change_your_account_password)
edit.add_command(label = "Change your account IP", command = Change_your_account_IP)
edit.add_separator()
edit.add_command(label = "Change your SERVER", command = Change_your_SERVER)
menubar.add_cascade(label = "Edit", menu = edit)

edit = Menu(menubar, tearoff = 0)
edit.add_command(label = "About System", command = About_System)
edit.add_command(label = "System Help", command = System_Help)
edit.add_command(label = "Application Help", command = Application_Help)
edit.add_separator()
edit.add_command(label = "Software Help", command = Software_Help)
menubar.add_cascade(label = "Help", menu = edit)

sc.config(menu = menubar)

scws = Button(sc, text="Smart Control With Sensor", height=btnsizeh, width=btnsizew,
                         activebackground="blue", command=btn_scws)
scwt = Button(sc, text="Smart Control With Timer", height=btnsizeh, width=btnsizew,
                         activebackground="red", command=btn_scwt)

scws.grid(row=0, column=0)
scwt.grid(row=0, column=1)


sc.mainloop()


# Programming By Ali Dehghan Chaharabi
# www.alidehghanchaharabi.info