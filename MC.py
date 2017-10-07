import os
from tkinter import *
from database import sql

def set_mode():
    smr = sql.Data("database/smarthome")
    action = smr.manualctrl_input(ID,r1.get(),r2.get(),r3.get(),r4.get(),r5.get(),r6.get())
    print (action)

def set_on():
    smr = sql.Data("database/smarthome")
    action = smr.manualctrl_input(ID,1,1,1,1,1,1)
    print (action)

def set_off():
    smr = sql.Data("database/smarthome")
    action = smr.manualctrl_input(ID,0,0,0,0,0,0)
    print (action)

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

mc = Tk()

icon = PhotoImage(file='../pictures/manualcontrol.png')
mc.tk.call('wm', 'iconphoto', mc._w, icon)

screen_width = mc.winfo_screenwidth()
screen_height = mc.winfo_screenheight()

mc.geometry("%sx%s+0+0"%(screen_width,screen_height))
mc.resizable(width=True, height=True)

mc.title("Smart Home System Software V 1.0.0 - Manual Control")

menubar = Menu(mc)

filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label = "Look", command = Look)
filemenu.add_command(label = "Restart", command = Restart)
filemenu.add_command(label = "Sleep", command = Sleep)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = mc.quit)
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

mc.config(menu = menubar)

con = sql.Data("database/smarthome")
relay = []
relay = con.manualctrl_read()
ID = relay[0] + 1

r1 = IntVar()
r1.set(relay[1])
Label(mc, text="Relay 1 : ",).grid(row=0, column=0)
Radiobutton(mc, text="ON", variable=r1, value=1).grid(row=0, column=1)
Radiobutton(mc, text="OFF", variable=r1, value=0).grid(row=1, column=1)

Label(mc, text="\t",).grid(row=0, column=2)

r2 = IntVar()
r2.set(relay[2])
Label(mc, text="Relay 2 : ",).grid(row=0, column=3)
Radiobutton(mc, text="ON", variable=r2, value=1).grid(row=0, column=4)
Radiobutton(mc, text="OFF", variable=r2, value=0).grid(row=1, column=4)

Label(mc, text="\t",).grid(row=0, column=5)

r3 = IntVar()
r3.set(relay[3])
Label(mc, text="Relay 3 : ",).grid(row=0, column=6)
Radiobutton(mc, text="ON", variable=r3, value=1).grid(row=0, column=7)
Radiobutton(mc, text="OFF", variable=r3, value=0).grid(row=1, column=7)

Label(mc, text="\t",).grid(row=0, column=8)

r4 = IntVar()
r4.set(relay[4])
Label(mc, text="Relay 4 : ",).grid(row=0, column=9)
Radiobutton(mc, text="ON", variable=r4, value=1).grid(row=0, column=10)
Radiobutton(mc, text="OFF", variable=r4, value=0).grid(row=1, column=10)

Label(mc, text="\t",).grid(row=0, column=11)

r5 = IntVar()
r5.set(relay[5])
Label(mc, text="Relay 5 : ",).grid(row=0, column=12)
Radiobutton(mc, text="ON", variable=r5, value=1).grid(row=0, column=13)
Radiobutton(mc, text="OFF", variable=r5, value=0).grid(row=1, column=13)

Label(mc, text="\t",).grid(row=0, column=14)

r6 = IntVar()
r6.set(relay[6])
Label(mc, text="Relay 6 : ",).grid(row=0, column=15)
Radiobutton(mc, text="ON", variable=r6, value=1).grid(row=0, column=16)
Radiobutton(mc, text="OFF", variable=r6, value=0).grid(row=1, column=16)

Label(mc, text="\t",).grid(row=2, column=2)
Label(mc, text="\t",).grid(row=3, column=2)

Button(mc, text="Set Mode", width=10, fg="black", command=set_mode).grid(row=4, column=0)
Button(mc, text="ON All", width=10, fg="black", command=set_on).grid(row=4, column=2)
Button(mc, text="OFF All", width=10, fg="black", command=set_off).grid(row=4, column=4)
Button(mc, text="Exit", width=10, fg="black", command=mc.destroy).grid(row=4, column=6)

mc.mainloop()


# Programming By Ali Dehghan Chaharabi
# www.alidehghanchaharabi.info