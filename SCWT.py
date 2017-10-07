import os
from tkinter import *
from database import sql

def first_set_time():
    con = sql.Data("database/smarthome")
    time = con.timer_read()
    global ID
    ID = time[0]  + 1
    time_s = time[1].split(",") + time[2].split(",") + time[3].split(",") + time[4].split(",") + time[5].split(",") + time[6].split(",")
    return time_s

def set_data():
    times_1 =  str(str(hro1.get()) + "," + str(mro1.get()) + "," + str(hrf1.get()) + "," + str(mrf1.get()))
    times_2 =  str(str(hro2.get()) + "," + str(mro2.get()) + "," + str(hrf2.get()) + "," + str(mrf2.get()))
    times_3 =  str(str(hro3.get()) + "," + str(mro3.get()) + "," + str(hrf3.get()) + "," + str(mrf3.get()))
    times_4 =  str(str(hro4.get()) + "," + str(mro4.get()) + "," + str(hrf4.get()) + "," + str(mrf4.get()))
    times_5 =  str(str(hro5.get()) + "," + str(mro5.get()) + "," + str(hrf5.get()) + "," + str(mrf5.get()))
    times_6 =  str(str(hro6.get()) + "," + str(mro6.get()) + "," + str(hrf6.get()) + "," + str(mrf6.get()))
    con = sql.Data("database/smarthome")
    action = con.timer_input(ID,times_1,times_2,times_3,times_4,times_5,times_6)
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
    
scwt = Tk()

sensor = LabelFrame(scwt, text="Timer")
sensor.pack(fill="both", expand="yes")

sensorinfo = LabelFrame(sensor, text="Timer Information")
sensorinfo.pack(fill="both", expand="yes")

sensorset = LabelFrame(sensor, text="Timer Set")
sensorset.pack(fill="both", expand="yes")


icon = PhotoImage(file='../pictures/smartcontrol.png')
scwt.tk.call('wm', 'iconphoto', scwt._w, icon)

screen_width = scwt.winfo_screenwidth()
screen_height = scwt.winfo_screenheight()

scwt.geometry("%sx%s+0+0"%(screen_width,screen_height))
scwt.resizable(width=True, height=True)

scwt.title("Smart Home System Software V 1.0.0 - Smart Control With Timer")

menubar = Menu(scwt)

filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label = "Look", command = Look)
filemenu.add_command(label = "Restart", command = Restart)
filemenu.add_command(label = "Sleep", command = Sleep)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = scwt.quit)
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

scwt.config(menu = menubar)

times = first_set_time()
print (times)
con = sql.Data("database/smarthome")
sens = []
sens = con.sensor_read()

#sens info :
Label(sensorinfo,font=("Calibri",20), text="Relay 1: %i" % (sens[17])).grid(row=0, column=0)
Label(sensorinfo,font=("Calibri",20), text="\tRelay 2: %i" % (sens[18])).grid(row=0, column=1)
Label(sensorinfo,font=("Calibri",20), text="\tRelay 3: %i" % (sens[19])).grid(row=0, column=2)
Label(sensorinfo,font=("Calibri",20), text="\tRelay 4: %i" % (sens[20])).grid(row=0, column=3)
Label(sensorinfo,font=("Calibri",20), text="\tRelay 5: %i" % (sens[21])).grid(row=0, column=4)
Label(sensorinfo,font=("Calibri",20), text="\tRelay 6: %i" % (sens[22])).grid(row=0, column=5)

Label(sensorinfo,font=("Calibri",10), text="ON Time: %i:%i" % (int(times[0]),int(times[1]))).grid(row=1, column=0)
Label(sensorinfo,font=("Calibri",10), text="\t\tON Time: %i:%i" % (int(times[4]),int(times[5]))).grid(row=1, column=1)
Label(sensorinfo,font=("Calibri",10), text="\t\tON Time: %i:%i" % (int(times[8]),int(times[9]))).grid(row=1, column=2)
Label(sensorinfo,font=("Calibri",10), text="\t\tON Time: %i:%i" % (int(times[12]),int(times[13]))).grid(row=1, column=3)
Label(sensorinfo,font=("Calibri",10), text="\t\tON Time: %i:%i" % (int(times[16]),int(times[17]))).grid(row=1, column=4)
Label(sensorinfo,font=("Calibri",10), text="\t\tON Time: %i:%i" % (int(times[20]),int(times[21]))).grid(row=1, column=5)

Label(sensorinfo,font=("Calibri",10), text="OFF Time: %i:%i" % (int(times[2]),int(times[3]))).grid(row=2, column=0)
Label(sensorinfo,font=("Calibri",10), text="\t\tOFF Time: %i:%i" % (int(times[6]),int(times[7]))).grid(row=2, column=1)
Label(sensorinfo,font=("Calibri",10), text="\t\tOFF Time: %i:%i" % (int(times[10]),int(times[11]))).grid(row=2, column=2)
Label(sensorinfo,font=("Calibri",10), text="\t\tOFF Time: %i:%i" % (int(times[14]),int(times[15]))).grid(row=2, column=3)
Label(sensorinfo,font=("Calibri",10), text="\t\tOFF Time: %i:%i" % (int(times[18]),int(times[19]))).grid(row=2, column=4)
Label(sensorinfo,font=("Calibri",10), text="\t\tOFF Time: %i:%i" % (int(times[22]),int(times[23]))).grid(row=2, column=5)

#sens set :
Label(sensorset, text="Relay 1",).grid(row=0, column=0)
hro1 = Scale(sensorset, from_=0, to=23, length=200, tickinterval=1)
hro1.set(int(times[0]))
hro1.grid(row=1, column=0)
mro1 = Scale(sensorset, from_=0, to=59, length=200, tickinterval=1)
mro1.set(int(times[1]))
mro1.grid(row=1, column=1)
hrf1 = Scale(sensorset, from_=0, to=23, length=200, tickinterval=1)
hrf1.set(int(times[2]))
hrf1.grid(row=2, column=0)
mrf1 = Scale(sensorset, from_=0, to=59, length=200, tickinterval=1)
mrf1.set(int(times[3]))
mrf1.grid(row=2, column=1)

Label(sensorset, text="\t",).grid(row=0, column=2)

Label(sensorset, text="Relay 2",).grid(row=0, column=3)
hro2 = Scale(sensorset, from_=0, to=23, length=200, tickinterval=1)
hro2.set(int(times[4]))
hro2.grid(row=1, column=3)
mro2 = Scale(sensorset, from_=0, to=59, length=200, tickinterval=1)
mro2.set(int(times[5]))
mro2.grid(row=1, column=4)
hrf2 = Scale(sensorset, from_=0, to=23, length=200, tickinterval=1)
hrf2.set(int(times[6]))
hrf2.grid(row=2, column=3)
mrf2 = Scale(sensorset, from_=0, to=59, length=200, tickinterval=1)
mrf2.set(int(times[7]))
mrf2.grid(row=2, column=4)

Label(sensorset, text="\t",).grid(row=0, column=5)

Label(sensorset, text="Relay 3",).grid(row=0, column=6)
hro3 = Scale(sensorset, from_=0, to=23, length=200, tickinterval=1)
hro3.set(int(times[8]))
hro3.grid(row=1, column=6)
mro3 = Scale(sensorset, from_=0, to=59, length=200, tickinterval=1)
mro3.set(int(times[9]))
mro3.grid(row=1, column=7)
hrf3 = Scale(sensorset, from_=0, to=23, length=200, tickinterval=1)
hrf3.set(int(times[10]))
hrf3.grid(row=2, column=6)
mrf3 = Scale(sensorset, from_=0, to=59, length=200, tickinterval=1)
mrf3.set(int(times[11]))
mrf3.grid(row=2, column=7)

Label(sensorset, text="\t",).grid(row=0, column=8)

Label(sensorset, text="Relay 4",).grid(row=0, column=9)
hro4 = Scale(sensorset, from_=0, to=23, length=200, tickinterval=1)
hro4.set(int(times[12]))
hro4.grid(row=1, column=9)
mro4 = Scale(sensorset, from_=0, to=59, length=200, tickinterval=1)
mro4.set(int(times[13]))
mro4.grid(row=1, column=10)
hrf4 = Scale(sensorset, from_=0, to=23, length=200, tickinterval=1)
hrf4.set(int(times[14]))
hrf4.grid(row=2, column=9)
mrf4 = Scale(sensorset, from_=0, to=59, length=200, tickinterval=1)
mrf4.set(int(times[15]))
mrf4.grid(row=2, column=10)

Label(sensorset, text="\t",).grid(row=0, column=11)

Label(sensorset, text="Relay 5",).grid(row=0, column=12)
hro5 = Scale(sensorset, from_=0, to=23, length=200, tickinterval=1)
hro5.set(int(times[16]))
hro5.grid(row=1, column=12)
mro5 = Scale(sensorset, from_=0, to=59, length=200, tickinterval=1)
mro5.set(int(times[17]))
mro5.grid(row=1, column=13)
hrf5 = Scale(sensorset, from_=0, to=23, length=200, tickinterval=1)
hrf5.set(int(times[18]))
hrf5.grid(row=2, column=12)
mrf5 = Scale(sensorset, from_=0, to=59, length=200, tickinterval=1)
mrf5.set(int(times[19]))
mrf5.grid(row=2, column=13)

Label(sensorset, text="\t",).grid(row=0, column=14)

Label(sensorset, text="Relay 6",).grid(row=0, column=15)
hro6 = Scale(sensorset, from_=0, to=23, length=200, tickinterval=1)
hro6.set(int(times[20]))
hro6.grid(row=1, column=15)
mro6 = Scale(sensorset, from_=0, to=59, length=200, tickinterval=1)
mro6.set(int(times[21]))
mro6.grid(row=1, column=16)
hrf6 = Scale(sensorset, from_=0, to=23, length=200, tickinterval=1)
hrf6.set(int(times[22]))
hrf6.grid(row=2, column=15)
mrf6 = Scale(sensorset, from_=0, to=59, length=200, tickinterval=1)
mrf6.set(int(times[23]))
mrf6.grid(row=2, column=16)

Label(sensorset, text="\t",).grid(row=0, column=17)

Button(sensorset, text="Set Time", height=5, width=20, fg="black", command=set_data).grid(row=1, column=18)
Button(sensorset, text="Exit", height=5, width=20, fg="black", command=exit).grid(row=2, column=18)
    
scwt.mainloop()

   
  


# Programming By Ali Dehghan Chaharabi
# www.alidehghanchaharabi.info

    
