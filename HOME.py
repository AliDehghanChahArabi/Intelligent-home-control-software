import os
import time
from tkinter import *
from database import sql

#system("toggle.fullscreen")

def sem_mode_system():
    localtime = time.asctime( time.localtime(time.time()) )
    set_m = sql.Data("database/smarthome")
    action = set_m.smode_input(ID, ctrl.get(),str(localtime))
    print (action)
    home.destroy()  

def btn_sc():
    print ("SC")
    os.startfile('SC.py')
def btn_mc():
    print ("MS")
    os.startfile('MC.py')
def btn_ss():
    print ("SS")
    os.startfile('SS.py')
def btn_in():
    print ("IN")
    os.startfile('IN.py')

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

while True:
    home = Tk()
    
    ctrlsystem = LabelFrame(home, text="System Mode ")
    ctrlsystem.pack(fill="both", expand="yes")

    labelframe = LabelFrame(home, text="Tools")
    labelframe.pack(fill="both", expand="yes")

    icon = PhotoImage(file='../pictures/homeicone.png')
    home.tk.call('wm', 'iconphoto', home._w, icon)

    screen_width = home.winfo_screenwidth()
    screen_height = home.winfo_screenheight()
    btnsizeh = int(screen_height/40)
    btnsizew = int(screen_height/8.5)
    home.geometry("%sx%s+0+0"%(screen_width,screen_height))
    home.resizable(width=True, height=True)

    home.title("Smart Home System Software V 1.0.0")

    menubar = Menu(home)

    filemenu = Menu(menubar, tearoff = 0)
    filemenu.add_command(label = "Look", command = Look)
    filemenu.add_command(label = "Restart", command = Restart)
    filemenu.add_command(label = "Sleep", command = Sleep)
    filemenu.add_separator()
    filemenu.add_command(label = "Exit", command = home.quit)
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

    home.config(menu = menubar)

    con = sql.Data("database/smarthome")
    ctrlm = con.smode_read()
    ID = ctrlm[0] + 1

    ctrl = IntVar()
    ctrl.set(ctrlm[1])
    Label(ctrlsystem,font=("Calibri",20), text="\t",).grid(row=0, column=0)
    Radiobutton(ctrlsystem,font=("Calibri",20), text="Smart Control With Sensor\t", variable=ctrl, value=1).grid(row=0, column=1)
    Radiobutton(ctrlsystem,font=("Calibri",20), text="Smart Control With Timer\t", variable=ctrl, value=2).grid(row=0, column=2)
    Radiobutton(ctrlsystem,font=("Calibri",20), text="Manual Cotrol\t", variable=ctrl, value=3).grid(row=0, column=3)
    sms = Button(ctrlsystem, text="Set Mode System", height=2, width=20, command=sem_mode_system).grid(row=0, column=4)

    sctrl = Button(labelframe, text="Smart Control", height=btnsizeh, width=btnsizew,
                             activebackground="green", command=btn_sc)
    mctrl = Button(labelframe, text="Manual Control", height=btnsizeh, width=btnsizew,
                             activebackground="red", command=btn_mc)
    status = Button(labelframe, text="Show Status", height=btnsizeh, width=btnsizew,
                             activebackground="blue", command=btn_ss)
    prints = Button(labelframe, text="Information", height=btnsizeh, width=btnsizew,
                             activebackground="yellow", command=btn_in)

    sctrl.grid(row=0, column=0)
    mctrl.grid(row=0, column=1)
    status.grid(row=1, column=0)
    prints.grid(row=1, column=1)

    home.mainloop()


# Programming By Ali Dehghan Chaharabi
# www.alidehghanchaharabi.info  
