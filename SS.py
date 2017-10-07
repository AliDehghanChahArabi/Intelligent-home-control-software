import os
import time
from tkinter import *
from database import sql

localtime = time.asctime( time.localtime(time.time()) )

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

ss = Tk()

icon = PhotoImage(file='../pictures/status.png')
ss.tk.call('wm', 'iconphoto', ss._w, icon)

screen_width = ss.winfo_screenwidth()
screen_height = ss.winfo_screenheight()

ss.geometry("%sx%s+0+0"%(screen_width,screen_height))
ss.resizable(width=True, height=True)

ss.title("Smart Home System Software V 1.0.0 - Show Status")

menubar = Menu(ss)

filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label = "Look", command = Look)
filemenu.add_command(label = "Restart", command = Restart)
filemenu.add_command(label = "Sleep", command = Sleep)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = ss.quit)
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

ss.config(menu = menubar)

Label(ss, text="Status Smart Home Systam\n\n",).grid(row=0, column=5)

con = sql.Data("database/smarthome")
sens = []
sens = con.sensor_read()

con1 = sql.Data("database/smarthome")
mode = []
mode = ctrlm = con1.smode_read()

if int(mode[1]) == 1 :
    modes = "Great - SC"
elif int(mode[1]) == 2 :
    modes = "Good - ST"
elif int(mode[1]) == 3 :
    modes = "Bad - Manual"

Label(ss, text="Temperature Sensor 1 :\t%i  C"%(sens[1])).grid(row=1, column=0)
Label(ss, text="Temperature Sensor 2 :\t%i  C"%(sens[2])).grid(row=2, column=0)
Label(ss, text="Temperature Sensor 3 :\t%i  C"%(sens[3])).grid(row=3, column=0)
Label(ss, text="Temperature Sensor 4 :\t%i  C"%(sens[4])).grid(row=4, column=0)

Label(ss, text="\t",).grid(row=0, column=1)

Label(ss, text="LDR Sensor 1 :\t%i  L"%(sens[5])).grid(row=1, column=2)
Label(ss, text="LDR Sensor 2 :\t%i  L"%(sens[6])).grid(row=2, column=2)
Label(ss, text="LDR Sensor 3 :\t%i  L"%(sens[7])).grid(row=3, column=2)
Label(ss, text="LDR Sensor 4 :\t%i  L"%(sens[8])).grid(row=4, column=2)

Label(ss, text="\t",).grid(row=0, column=3)
Label(ss, text="\t",).grid(row=0, column=4)
Label(ss, text="\t",).grid(row=0, column=6)
Label(ss, text="\t",).grid(row=0, column=7)

Label(ss, text="Window Sensor 1 :\t%i"%(sens[9])).grid(row=1, column=8)
Label(ss, text="Window Sensor 2 :\t%i"%(sens[10])).grid(row=2, column=8)
Label(ss, text="Window Sensor 3 :\t%i"%(sens[11])).grid(row=3, column=8)
Label(ss, text="Window Sensor 4 :\t%i"%(sens[12])).grid(row=4, column=8)

Label(ss, text="\t",).grid(row=0, column=9)

Label(ss, text="Door Sensor 1 :\t%i"%(sens[13])).grid(row=1, column=10)
Label(ss, text="Door Sensor 2 :\t%i"%(sens[14])).grid(row=2, column=10)
Label(ss, text="Door Sensor 3 :\t%i"%(sens[15])).grid(row=3, column=10)
Label(ss, text="Door Sensor 4 :\t%i"%(sens[16])).grid(row=4, column=10)

Label(ss, text="\t",).grid(row=5, column=0)

if int(sens[17]) == 1:
    r1 = "ON"
else :
    r1 = "OFF"

if int(sens[18]) == 1:
    r2 = "ON"
else :
    r2 = "OFF"

if int(sens[19]) == 1:
    r3 = "ON"
else :
    r3 = "OFF"

if int(sens[20]) == 1:
    r4 = "ON"
else :
    r4 = "OFF"

if int(sens[21]) == 1:
    r5 = "ON"
else :
    r5 = "OFF"

if int(sens[22]) == 1:
    r6 = "ON"
else :
    r6 = "OFF"

Label(ss, text="Relay 1 :\t%s\t\t"%(r1)).grid(row=6, column=0)
Label(ss, text="Relay 2 :\t%s\t\t"%(r2)).grid(row=7, column=0)
Label(ss, text="Relay 3 :\t%s\t\t"%(r3)).grid(row=8, column=0)
Label(ss, text="Relay 4 :\t%s\t\t"%(r4)).grid(row=9, column=0)
Label(ss, text="Relay 5 :\t%s\t\t"%(r5)).grid(row=10, column=0)
Label(ss, text="Relay 6 :\t%s\t\t"%(r6)).grid(row=11, column=0)

Label(ss, text="\t",).grid(row=5, column=1)

con1 = sql.Data("database/smarthome")
info = []
info = con1.info_read()

Label(ss, text="Operator :\t%s\t\t"%(info[1])).grid(row=6, column=2)
Label(ss, text="Device serial :\t%s\t\t\t"%(info[6])).grid(row=7, column=2)
Label(ss, text="Date and Time :\t%s\t\t"%(str(localtime))).grid(row=8, column=2)
Label(ss, text="System Status :\t%s\t\t\t"%(modes)).grid(row=9, column=2)
Label(ss, text="Device Temperature :\t%i C\t\t\t"%(sens[1])).grid(row=10, column=2)
Label(ss, text="Network connection type :\t%s\t\t\t"%("LAN")).grid(row=11, column=2)


#Label(ss, text="\t",).grid(row=2, column=2)
#Label(ss, text="\t",).grid(row=3, column=2)

Button(ss, text="Print", width=10, fg="black", command="").grid(row=7, column=6)
Button(ss, text="Save", width=10, fg="black", command="").grid(row=7, column=7)
Button(ss, text="Send", width=10, fg="black", command="").grid(row=8, column=6)
Button(ss, text="Exit", width=10, fg="black", command=ss.destroy).grid(row=8, column=7)

ss.mainloop()


# Programming By Ali Dehghan Chaharabi
# www.alidehghanchaharabi.info