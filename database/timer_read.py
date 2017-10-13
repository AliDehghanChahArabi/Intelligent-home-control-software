import sqlite3

conn = sqlite3.connect('smarthome.db')

#Tabel
"""conn.execute('''CREATE TABLE TIMER
       (ID INT PRIMARY KEY     NOT NULL,
        T1           TEXT    NOT NULL,
        T2           TEXT    NOT NULL,
        T3           TEXT    NOT NULL,
        T4           TEXT    NOT NULL,
        T5           TEXT    NOT NULL,
        T6           TEXT    NOT NULL);''')
print ("Table created successfully")"""

#read data
cursor = conn.execute("SELECT T1,T2,T3,T4,T5,T6 from TIMER")
for i in cursor :
    print (i)  
conn.close()


# Programming By Ali Dehghan Chaharabi
# www.alidehghanchaharabi.info