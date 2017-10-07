import os
from tkinter import *
from database import sql

global ID_resolution

def setdata (): 
    con = sql.Data("database/smarthome")
    set_data = con.resolution_input(ID_resolution,mST1.get(),MST1.get(),mST2.get(),MST2.get(),mST3.get(), MST3.get(),mST4.get(), MST4.get(),mSL1.get(), MSL1.get(), mSL2.get(), MSL2.get(),mSL3.get(), MSL3.get(), mSL4.get(), MSL4.get(),mSW1.get(), MSW1.get(), mSW2.get(), MSW2.get(),mSW3.get(),MSW3.get(),mSW4.get(), MSW4.get(),mSD1.get(), MSD1.get(), mSD2.get(), MSD2.get(), mSD3.get(), MSD3.get(),mSD4.get(), MSD4.get())
    print (set_data)
    

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
    
scws = Tk()

sensor = LabelFrame(scws, text="Sensor")
sensor.pack(fill="both", expand="yes")

sensorinfo = LabelFrame(sensor, text="Sensor Information")
sensorinfo.pack(fill="both", expand="yes")

sensorset = LabelFrame(sensor, text="Sensor Set")
sensorset.pack(fill="both", expand="yes")


icon = PhotoImage(file='../pictures/smartcontrol.png')
scws.tk.call('wm', 'iconphoto', scws._w, icon)

screen_width = scws.winfo_screenwidth()
screen_height = scws.winfo_screenheight()

scws.geometry("%sx%s+0+0"%(screen_width,screen_height))
scws.resizable(width=True, height=True)

scws.title("Smart Home System Software V 1.0.0 - Smart Control With Sensor")

menubar = Menu(scws)

filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label = "Look", command = Look)
filemenu.add_command(label = "Restart", command = Restart)
filemenu.add_command(label = "Sleep", command = Sleep)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = scws.quit)
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

scws.config(menu = menubar)

con = sql.Data("database/smarthome")
sens = []
sens = con.sensor_read()
print (sens)

#sens info :
Label(sensorinfo,font=("Calibri",20), text="ST 1     : %i" % (sens[1])).grid(row=0, column=0)
Label(sensorinfo,font=("Calibri",20), text="\tST 2     : %i" % (sens[2])).grid(row=0, column=1)
Label(sensorinfo,font=("Calibri",20), text="\tST 3     : %i" % (sens[3])).grid(row=0, column=2)
Label(sensorinfo,font=("Calibri",20), text="\tST 4     : %i" % (sens[4])).grid(row=0, column=3)

Label(sensorinfo,font=("Calibri",20), text="SL 1     : %i" % (sens[5])).grid(row=1, column=0)
Label(sensorinfo,font=("Calibri",20), text="\tSL 2     : %i" % (sens[6])).grid(row=1, column=1)
Label(sensorinfo,font=("Calibri",20), text="\tSL 3     : %i" % (sens[7])).grid(row=1, column=2)
Label(sensorinfo,font=("Calibri",20), text="\tSL 4     : %i" % (sens[8])).grid(row=1, column=3)

Label(sensorinfo,font=("Calibri",20), text="SW 1   : %i" % (sens[9])).grid(row=2, column=0)
Label(sensorinfo,font=("Calibri",20), text="\tSW 2   : %i" % (sens[10])).grid(row=2, column=1)
Label(sensorinfo,font=("Calibri",20), text="\tSW 3   : %i" % (sens[11])).grid(row=2, column=2)
Label(sensorinfo,font=("Calibri",20), text="\tSW 4   : %i" % (sens[12])).grid(row=2, column=3)

Label(sensorinfo,font=("Calibri",20), text="SD 1     : %i" % (sens[13])).grid(row=3, column=0)
Label(sensorinfo,font=("Calibri",20), text="\tSD 2     : %i" % (sens[14])).grid(row=3, column=1)
Label(sensorinfo,font=("Calibri",20), text="\tSD 3     : %i" % (sens[15])).grid(row=3, column=2)
Label(sensorinfo,font=("Calibri",20), text="\tSD 4     : %i" % (sens[16])).grid(row=3, column=3)

Label(sensorinfo,font=("Calibri",20), text="Relay 1: %i" % (sens[17])).grid(row=4, column=0)
Label(sensorinfo,font=("Calibri",20), text="\tRelay 2: %i" % (sens[18])).grid(row=4, column=1)
Label(sensorinfo,font=("Calibri",20), text="\tRelay 3: %i" % (sens[19])).grid(row=4, column=2)
Label(sensorinfo,font=("Calibri",20), text="\tRelay 4: %i" % (sens[20])).grid(row=4, column=3)
Label(sensorinfo,font=("Calibri",20), text="\tRelay 5: %i" % (sens[21])).grid(row=4, column=4)
Label(sensorinfo,font=("Calibri",20), text="\tRelay 6: %i" % (sens[22])).grid(row=4, column=5)

con = sql.Data("database/smarthome")
resolution = []
resolution = con.resolution_read()
print (resolution)
ID_resolution = (resolution[0] + 1)
#sens set :
Label(sensorset, text="ST 1",).grid(row=0, column=0)
mST1 = Scale(sensorset, from_=0, to=100, length=80, tickinterval=1)
mST1.set(resolution[1])
mST1.grid(row=1, column=0)
MST1 = Scale(sensorset, from_=0, to=100, length=80, tickinterval=1)
MST1.set(resolution[2])
MST1.grid(row=1, column=1)

Label(sensorset, text="ST 2",).grid(row=2, column=0)
mST2 = Scale(sensorset, from_=0, to=100, length=80, tickinterval=1)
mST2.set(resolution[3])
mST2.grid(row=3, column=0)
MST2 = Scale(sensorset, from_=0, to=100, length=80, tickinterval=1)
MST2.set(resolution[4])
MST2.grid(row=3, column=1)

Label(sensorset, text="ST 3",).grid(row=4, column=0)
mST3 = Scale(sensorset, from_=0, to=100, length=80, tickinterval=1)
mST3.set(resolution[5])
mST3.grid(row=5, column=0)
MST3 = Scale(sensorset, from_=0, to=100, length=80, tickinterval=1)
MST3.set(resolution[6])
MST3.grid(row=5, column=1)

Label(sensorset, text="ST 4",).grid(row=6, column=0)
mST4 = Scale(sensorset, from_=0, to=100, length=80, tickinterval=1)
mST4.set(resolution[7])
mST4.grid(row=7, column=0)
MST4 = Scale(sensorset, from_=0, to=100, length=80, tickinterval=1)
MST4.set(resolution[8])
MST4.grid(row=7, column=1)

Label(sensorset, text="\t",).grid(row=0, column=2)
#
Label(sensorset, text="SL 1",).grid(row=0, column=3)
mSL1 = Scale(sensorset, from_=0, to=100, length=80, tickinterval=1)
mSL1.set(resolution[9])
mSL1.grid(row=1, column=3)
MSL1 = Scale(sensorset, from_=0, to=100, length=80, tickinterval=1)
MSL1.set(resolution[10])
MSL1.grid(row=1, column=4)

Label(sensorset, text="SL 2",).grid(row=2, column=3)
mSL2 = Scale(sensorset, from_=0, to=100, length=80, tickinterval=1)
mSL2.set(resolution[11])
mSL2.grid(row=3, column=3)
MSL2 = Scale(sensorset, from_=0, to=100, length=80, tickinterval=1)
MSL2.set(resolution[12])
MSL2.grid(row=3, column=4)

Label(sensorset, text="SL 3",).grid(row=4, column=3)
mSL3 = Scale(sensorset, from_=0, to=100, length=80, tickinterval=1)
mSL3.set(resolution[13])
mSL3.grid(row=5, column=3)
MSL3 = Scale(sensorset, from_=0, to=100, length=80, tickinterval=1)
MSL3.set(resolution[14])
MSL3.grid(row=5, column=4)

Label(sensorset, text="SL 4",).grid(row=6, column=3)
mSL4 = Scale(sensorset, from_=0, to=100, length=80, tickinterval=1)
mSL4.set(resolution[15])
mSL4.grid(row=7, column=3)
MSL4 = Scale(sensorset, from_=0, to=100, length=80, tickinterval=1)
MSL4.set(resolution[16])
MSL4.grid(row=7, column=4)

Label(sensorset, text="\t",).grid(row=0, column=5)
#
Label(sensorset, text="SW 1",).grid(row=0, column=6)
mSW1 = Scale(sensorset, from_=0, to=100, length=80, tickinterval=1)
mSW1.set(resolution[17])
mSW1.grid(row=1, column=6)
MSW1 = Scale(sensorset, from_=0, to=100, length=80, tickinterval=1)
MSW1.set(resolution[18])
MSW1.grid(row=1, column=7)

Label(sensorset, text="SW 2",).grid(row=2, column=6)
mSW2 = Scale(sensorset, from_=0, to=100, length=80, tickinterval=1)
mSW2.set(resolution[19])
mSW2.grid(row=3, column=6)
MSW2 = Scale(sensorset, from_=0, to=100, length=80, tickinterval=1)
MSW2.set(resolution[20])
MSW2.grid(row=3, column=7)

Label(sensorset, text="SW 3",).grid(row=4, column=6)
mSW3 = Scale(sensorset, from_=0, to=100, length=80, tickinterval=1)
mSW3.set(resolution[21])
mSW3.grid(row=5, column=6)
MSW3 = Scale(sensorset, from_=0, to=100, length=80, tickinterval=1)
MSW3.set(resolution[22])
MSW3.grid(row=5, column=7)

Label(sensorset, text="SW 4",).grid(row=6, column=6)
mSW4 = Scale(sensorset, from_=0, to=100, length=80, tickinterval=1)
mSW4.set(resolution[23])
mSW4.grid(row=7, column=6)
MSW4 = Scale(sensorset, from_=0, to=100, length=80, tickinterval=1)
MSW4.set(resolution[24])
MSW4.grid(row=7, column=7)

Label(sensorset, text="\t",).grid(row=0, column=8)
#
Label(sensorset, text="SD 1",).grid(row=0, column=9)
mSD1 = Scale(sensorset, from_=0, to=100, length=80, tickinterval=1)
mSD1.set(resolution[25])
mSD1.grid(row=1, column=9)
MSD1 = Scale(sensorset, from_=0, to=100, length=80, tickinterval=1)
MSD1.set(resolution[26])
MSD1.grid(row=1, column=10)

Label(sensorset, text="SD 2",).grid(row=2, column=9)
mSD2 = Scale(sensorset, from_=0, to=100, length=80, tickinterval=1)
mSD2.set(resolution[27])
mSD2.grid(row=3, column=9)
MSD2 = Scale(sensorset, from_=0, to=100, length=80, tickinterval=1)
MSD2.set(resolution[28])
MSD2.grid(row=3, column=10)

Label(sensorset, text="SD 3",).grid(row=4, column=9)
mSD3 = Scale(sensorset, from_=0, to=100, length=80, tickinterval=1)
mSD3.set(resolution[29])
mSD3.grid(row=5, column=9)
MSD3 = Scale(sensorset, from_=0, to=100, length=80, tickinterval=1)
MSD3.set(resolution[30])
MSD3.grid(row=5, column=10)

Label(sensorset, text="SD 4",).grid(row=6, column=9)
mSD4 = Scale(sensorset, from_=0, to=100, length=80, tickinterval=1)
mSD4.set(resolution[31])
mSD4.grid(row=7, column=9)
MSD4 = Scale(sensorset, from_=0, to=100, length=80, tickinterval=1)
MSD4.set(resolution[32])
MSD4.grid(row=7, column=10)


Label(sensorset, text="\t",).grid(row=1, column=14)


Button(sensorset, text="Set Resolution", height=5, width=20, fg="black", command=setdata).grid(row=1, column=15)
Button(sensorset, text="Exit", height=5, width=20, fg="black", command=exit).grid(row=1, column=16)
    
scws.mainloop()

   


# Programming By Ali Dehghan Chaharabi
# www.alidehghanchaharabi.info  


    
