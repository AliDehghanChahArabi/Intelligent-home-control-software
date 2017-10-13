import sqlite3

conn = sqlite3.connect('smarthome.db')

#Tabel
"""conn.execute('''CREATE TABLE MANUALCTRL
       (ID INT PRIMARY KEY     NOT NULL,
        R1           INT    NOT NULL,
        R2           INT    NOT NULL,
        R3           INT    NOT NULL,
        R4           INT    NOT NULL,
        R5           INT    NOT NULL,
        R6           INT    NOT NULL);''')
print ("Table created successfully")"""

#read data
cursor = conn.execute("SELECT ID,R1,R2,R3,R4,R5,R6 from MANUALCTRL")
for i in cursor :
    print (i)  
    
conn.close()


# Programming By Ali Dehghan Chaharabi
# www.alidehghanchaharabi.info