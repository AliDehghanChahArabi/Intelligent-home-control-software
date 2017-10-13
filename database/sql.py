import sqlite3

class Data():
    def __init__ (self, dbname):
        print (str(dbname) + ".db")
        self.conn = sqlite3.connect(str(dbname+".db"))

    def info_input(self, ID, NAME, PHONE, ADDRESS,USERNAME, PASSWORD, SERIAL, IDS, IPS, VERSION, LICENSE, YEARL):
        self.conn.execute("INSERT INTO INFORMATION(ID, NAME, PHONE, ADDRESS,USERNAME, PASSWORD, SERIAL, IDS, IPS, VERSION, LICENSE, YEARL)\
            VALUES (%i, '%s', %d, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', %d)" % (int(ID),NAME, int(PHONE), ADDRESS,USERNAME, PASSWORD, SERIAL, IDS, IPS, VERSION, LICENSE, int(YEARL)));
        self.conn.commit()
        self.conn.close()
        print ("import ok")
        return "OK"

    def info_read(self):
        cursor = self.conn.execute("SELECT ID, NAME, PHONE, ADDRESS,USERNAME, PASSWORD, SERIAL, IDS, IPS, VERSION, LICENSE, YEARL from INFORMATION")
        data = ()
        for i in cursor :
            print (i)
            data= i
        self.conn.close()
        return data

    def manualctrl_input(self,ID,R1,R2,R3,R4,R5,R6):
        self.conn.execute("INSERT INTO MANUALCTRL (ID,R1,R2,R3,R4,R5,R6) \
            VALUES (%i,%i,%i,%i,%i,%i,%i)" % (int(ID),int(R1),int(R2),int(R3),int(R4),int(R5),int(R6)));
        self.conn.commit()
        self.conn.close()
        print ("import ok")
        return "OK"

    def manualctrl_read(self):
        cursor = self.conn.execute("SELECT ID,R1,R2,R3,R4,R5,R6 from MANUALCTRL")
        data = ()
        for i in cursor :
            print (i)
            data = i
        self.conn.close()
        return data

    def sensor_input(self,ID ,ST1 ,ST2 ,ST3 ,ST4 ,SL1 ,SL2 ,SL3 ,SL4 ,SW1 ,SW2 ,SW3 ,SW4 ,SD1 ,SD2 ,SD3 ,SD4 ,R1 ,R2 ,R3 ,R4 ,R5 ,R6):
        self.conn.execute("INSERT INTO SENSORDATA (ID ,ST1 ,ST2 ,ST3 ,ST4 ,SL1 ,SL2 ,SL3 ,SL4 ,SW1 ,SW2 ,SW3 ,SW4 ,SD1 ,SD2 ,SD3 ,SD4 ,R1 ,R2 ,R3 ,R4 ,R5 ,R6) \
            VALUES (%i,%i,%i,%i,%i,%i,%i,%i,%i,%i,%i,%i,%i,%i,%i,%i,%i,%i,%i,%i,%i,%i,%i)" % (int(ID) ,int(ST1) ,int(ST2) ,int(ST3) ,int(ST4) ,int(SL1) ,int(SL2) ,int(SL3) ,int(SL4) ,int(SW1) ,int(SW2) ,int(SW3) ,int(SW4) ,int(SD1) ,int(SD2) ,int(SD3) ,int(SD4) ,int(R1) ,int(R2) ,int(R3) ,int(R4) ,int(R5) ,int(R6)));
        self.conn.commit()
        self.conn.close()
        print ("import ok")
        return "OK"

    def sensor_read(self):
        cursor = self.conn.execute("SELECT ID ,ST1 ,ST2 ,ST3 ,ST4 ,SL1 ,SL2 ,SL3 ,SL4 ,SW1 ,SW2 ,SW3 ,SW4 ,SD1 ,SD2 ,SD3 ,SD4 ,R1 ,R2 ,R3 ,R4 ,R5 ,R6 from SENSORDATA")
        data = ()
        for i in cursor :
            print (i)
            data = i
        self.conn.close()
        return data

    def smartctrl_input (self,ID,SCSR1A,SCSR1B,SCSR2A,SCSR2B,SCSR3A,SCSR3B,SCSR4A,SCSR4B,SCSR5A,SCSR5B,SCSR6A,SCSR6B,SCTR1A,SCTR1B,SCTR1C,SCTR1D,SCTR2A,SCTR2B,SCTR2C,SCTR2D,SCTR3A,SCTR3B,SCTR3C,SCTR3D,SCTR4A,SCTR4B,SCTR4C,SCTR4D,SCTR5A,SCTR5B,SCTR5C,SCTR5D,SCTR6A,SCTR6B,SCTR6C,SCTR6D):
        self.conn.execute("INSERT INTO SMARTCTRL (ID,SCSR1A,SCSR1B,SCSR2A,SCSR2B,SCSR3A,SCSR3B,SCSR4A,SCSR4B,SCSR5A,SCSR5B,SCSR6A,SCSR6B,SCTR1A,SCTR1B,SCTR1C,SCTR1D,SCTR2A,SCTR2B,SCTR2C,SCTR2D,SCTR3A,SCTR3B,SCTR3C,SCTR3D,SCTR4A,SCTR4B,SCTR4C,SCTR4D,SCTR5A,SCTR5B,SCTR5C,SCTR5D,SCTR6A,SCTR6B,SCTR6C,SCTR6D) \
            VALUES (%i,%i,%i,%i,%i,%i,%i,%i,%i,%i,%i,%i,%i,%i,%i,%i,%i,%i,%i,%i,%i,%i,%i,%i,%i,%i,%i,%i,%i,%i,%i,%i,%i,%i,%i,%i,%i)" % (int(ID),int(SCSR1A),int(SCSR1B),int(SCSR2A),int(SCSR2B),int(SCSR3A),int(SCSR3B),int(SCSR4A),int(SCSR4B),int(SCSR5A),int(SCSR5B),int(SCSR6A),int(SCSR6B),int(SCTR1A),int(SCTR1B),int(SCTR1C),int(SCTR1D),int(SCTR2A),int(SCTR2B),int(SCTR2C),int(SCTR2D),int(SCTR3A),int(SCTR3B),int(SCTR3C),int(SCTR3D),int(SCTR4A),int(SCTR4B),int(SCTR4C),int(SCTR4D),int(SCTR5A),int(SCTR5B),int(SCTR5C),int(SCTR5D),int(SCTR6A),int(SCTR6B),int(SCTR6C),int(SCTR6D)));
        self.conn.commit()
        self.conn.close()
        print ("import ok")
        return "OK"

    def smartctrl_read(self):
        cursor = self.conn.execute("SELECT ID,SCSR1A,SCSR1B,SCSR2A,SCSR2B,SCSR3A,SCSR3B,SCSR4A,SCSR4B,SCSR5A,SCSR5B,SCSR6A,SCSR6B,SCTR1A,SCTR1B,SCTR1C,SCTR1D,SCTR2A,SCTR2B,SCTR2C,SCTR2D,SCTR3A,SCTR3B,SCTR3C,SCTR3D,SCTR4A,SCTR4B,SCTR4C,SCTR4D,SCTR5A,SCTR5B,SCTR5C,SCTR5D,SCTR6A,SCTR6B,SCTR6C,SCTR6D from SMARTCTRL")
        data = ()
        for i in cursor :
            print (i)
            data = i
        self.conn.close()
        return data

    def resolution_input (self,ID,nST1,MST1,nST2,MST2,nST3,MST3,nST4,MST4,nSL1,MSL1,nSL2,MSL2,nSL3,MSL3,nSL4,MSL4,nSW1,MSW1,nSW2,MSW2,nSW3,MSW3,nSW4,MSW4,nSD1,MSD1,nSD2,MSD2,nSD3,MSD3,nSD4,MSD4):
        self.conn.execute("INSERT INTO RESOLUTION (ID,nST1,MST1,nST2,MST2,nST3,MST3,nST4,MST4,nSL1,MSL1,nSL2,MSL2,nSL3,MSL3,nSL4,MSL4,nSW1,MSW1,nSW2,MSW2,nSW3,MSW3,nSW4,MSW4,nSD1,MSD1,nSD2,MSD2,nSD3,MSD3,nSD4,MSD4) \
            VALUES (%i,%i,%i,%i,%i,%i,%i,%i,%i,%i,%i,%i,%i,%i,%i,%i,%i,%i,%i,%i,%i,%i,%i,%i,%i,%i,%i,%i,%i,%i,%i,%i,%i)" % (int(ID),int(nST1),int(MST1),int(nST2),int(MST2),int(nST3),int(MST3),int(nST4),int(MST4),int(nSL1),int(MSL1),int(nSL2),int(MSL2),int(nSL3),int(MSL3),int(nSL4),int(MSL4),int(nSW1),int(MSW1),int(nSW2),int(MSW2),int(nSW3),int(MSW3),int(nSW4),int(MSW4),int(nSD1),int(MSD1),int(nSD2),int(MSD2),int(nSD3),int(MSD3),int(nSD4),int(MSD4)));
        self.conn.commit()
        self.conn.close()
        print ("import ok")
        return "OK"

    def resolution_read (self):
        cursor = self.conn.execute("SELECT ID,nST1,MST1,nST2,MST2,nST3,MST3,nST4,MST4,nSL1,MSL1,nSL2,MSL2,nSL3,MSL3,nSL4,MSL4,nSW1,MSW1,nSW2,MSW2,nSW3,MSW3,nSW4,MSW4,nSD1,MSD1,nSD2,MSD2,nSD3,MSD3,nSD4,MSD4 from RESOLUTION")
        data = ()
        for i in cursor :
            print (i)
            data = i
        self.conn.close()
        return data

    def timer_input (self, ID,T1,T2,T3,T4,T5,T6):
         self.conn.execute("INSERT INTO TIMER(ID, T1,T2,T3,T4,T5,T6)\
            VALUES (%i, '%s', '%s', '%s', '%s', '%s', '%s')" % (int(ID),str(T1),str(T2),str(T3),str(T4),str(T5),str(T6)));
         self.conn.commit()
         self.conn.close()
         print ("import ok")
         return "OK"

    def timer_read (self):
        cursor = self.conn.execute("SELECT ID,T1,T2,T3,T4,T5,T6 from TIMER")
        data = ()
        for i in cursor :
            print (i)
            data = i
        self.conn.close()
        return data

    def smode_input (self,ID, mode, date):
         self.conn.execute("INSERT INTO SYSTEMMODE(ID, mode, date)\
            VALUES (%i, %i, '%s')" % (int(ID),int(mode),str(date)));
         self.conn.commit()
         self.conn.close()
         print ("import ok")
         return "OK"

    def smode_read (self):
        cursor = self.conn.execute("SELECT ID, mode, date from SYSTEMMODE")
        data = ()
        for i in cursor :
            print (i)
            data = i
        self.conn.close()
        return data
        

info = Data("smarthome")
#info.info_input("3","Ghasem Gholikhani", "09122566506", "Tehran-IRAN", "ghgholikhani", "inahkilohghg", "ipmm1212adch", "12", "123.123.12.1", "1.0.0", "iPMM Co.", 2)
#print (info.info_read())
#print(info.manualctrl_input(3,0,1,1,0,1,1))
#print(info.manualctrl_read())
#info.sensor_input(2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)
#print(info.sensor_read())
#info.smartctrl_input(2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
#print(info.smartctrl_read())
#print(info.resolution_input(4, 2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,100,20,21,22,23,24,25,26,27,28,29,30,31,32,33))
#print(info.resolution_read())
#print(info.timer_input(2,"11","11","11","11","11","11"))
#print(info.timer_read())
#print(info.smode_input(2,1, "ss"))
#print(info.smode_read())


# Programming By Ali Dehghan Chaharabi
# www.alidehghanchaharabi.info