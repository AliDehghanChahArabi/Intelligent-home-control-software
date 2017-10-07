import os
from tkinter import *
from database import sql

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

info = Tk()

icon = PhotoImage(file='../pictures/information.png')
info.tk.call('wm', 'iconphoto', info._w, icon)

lg = LabelFrame(info, text="")
lg.pack(fill="both")

labelframe = LabelFrame(info, text="Information")
labelframe.pack(fill="both")

screen_width = info.winfo_screenwidth()
screen_height = info.winfo_screenheight()
    
info.geometry("%sx%s+0+0"%(screen_width,screen_height))
info.resizable(width=True, height=True)

info.title("Smart Home System Software V 1.0.0 - Information")

menubar = Menu(info)

filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label = "Look", command = Look)
filemenu.add_command(label = "Restart", command = Restart)
filemenu.add_command(label = "Sleep", command = Sleep)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = info.quit)
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

info.config(menu = menubar)

con = sql.Data("database/smarthome")
infor = []
infor = con.info_read()

user = PhotoImage(file="../pictures/user.png")
userpic = Label(lg, image=user).pack(side="right", anchor = "ne")

logo = PhotoImage(file="../pictures/logo.png")
logopic = Label(lg, image=logo).pack(side="left",anchor = "n")

Label(labelframe, text="Fist/Last Name : \t%s"%(infor[1])).pack(anchor = "nw")
#Label(info, text="Last Name : \tDehghan Chaharabi",).pack(anchor = "nw")
Label(labelframe, text="Phone No. : \t%i"%(infor[2])).pack(anchor = "nw")
Label(labelframe, text="Address : %s"%(infor[3])).pack(anchor = "nw")

Label(labelframe, text="\t",).pack(anchor = "nw")

Label(labelframe, text="User Name : \t%s"%(infor[4])).pack(anchor = "nw")
Label(labelframe, text="Password No. : \t%s"%(infor[5])).pack(anchor = "nw")

Label(labelframe, text="\t",).pack(anchor = "nw")

Label(labelframe, text="System serial : \t%s"%(infor[6])).pack(anchor = "nw")
Label(labelframe, text="System ID : \t%s"%(infor[7])).pack(anchor = "nw")
Label(labelframe, text="System IP : \t%s"%(infor[8])).pack(anchor = "nw")
Label(labelframe, text="System Version : \t%s"%(infor[9])).pack(anchor = "nw")
Label(labelframe, text="System License : \t%s"%(infor[10])).pack(anchor = "nw")
Label(labelframe, text="License Date : \t%i year"%(infor[11])).pack(anchor = "nw")


Label(info, text="\t",).pack(anchor = "nw")

Button(info, text="Buy licensing", width=20, fg="black", command="").pack(side="left",anchor = "ne")
Button(info, text="Exit", width=20, fg="black", command=info.destroy).pack(side="left",anchor = "ne")

    
info.mainloop()



# Programming By Ali Dehghan Chaharabi
# www.alidehghanchaharabi.info    
