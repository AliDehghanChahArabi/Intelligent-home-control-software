import sqlite3

conn = sqlite3.connect('smarthome.db')

#Tabel
"""conn.execute('''CREATE TABLE SYSTEMMODE
       (ID INT PRIMARY KEY     NOT NULL,
        mode           INT    NOT NULL,
        date            TEXT     NOT NULL);''')
print ("Table created successfully")"""

#read data
cursor = conn.execute("SELECT ID, mode, date from SYSTEMMODE")
for i in cursor :
    print (i)  
    
conn.close()


# Programming By Ali Dehghan Chaharabi
# www.alidehghanchaharabi.info