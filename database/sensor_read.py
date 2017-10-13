import sqlite3

conn = sqlite3.connect('smarthome.db')

#Tabel
"""conn.execute('''CREATE TABLE SENSORDATA
       (ID INT PRIMARY KEY     NOT NULL,
        ST1           INT    NOT NULL,
        ST2           INT    NOT NULL,
        ST3           INT    NOT NULL,
        ST4           INT    NOT NULL,
        SL1           INT    NOT NULL,
        SL2           INT    NOT NULL,
        SL3           INT    NOT NULL,
        SL4           INT    NOT NULL,
        SW1           INT    NOT NULL,
        SW2           INT    NOT NULL,
        SW3           INT    NOT NULL,
        SW4           INT    NOT NULL,
        SD1           INT    NOT NULL,
        SD2           INT    NOT NULL,
        SD3           INT    NOT NULL,
        SD4           INT    NOT NULL,
        R1           INT    NOT NULL,
        R2           INT    NOT NULL,
        R3           INT    NOT NULL,
        R4           INT    NOT NULL,
        R5           INT    NOT NULL,
        R6           INT    NOT NULL);''')
print ("Table created successfully")"""

#read data
cursor = conn.execute("SELECT ID ,ST1 ,ST2 ,ST3 ,ST4 ,SL1 ,SL2 ,SL3 ,SL4 ,SW1 ,SW2 ,SW3 ,SW4 ,SD1 ,SD2 ,SD3 ,SD4 ,R1 ,R2 ,R3 ,R4 ,R5 ,R6 from SENSORDATA")
for i in cursor :
    print (i)  
    
conn.close()


# Programming By Ali Dehghan Chaharabi
# www.alidehghanchaharabi.info