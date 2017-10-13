import sqlite3

conn = sqlite3.connect('smarthome.db')

#Tabel
"""conn.execute('''CREATE TABLE INFORMATION
       (ID INT PRIMARY KEY     NOT NULL,
        NAME           TEXT    NOT NULL,
        PHONE            INT     NOT NULL,
        ADDRESS        CHAR(50),
        USERNAME        CHAR(50),
        PASSWORD        CHAR(50),
        SERIAL        CHAR(50),
        IDS        CHAR(50),
        IPS        CHAR(50),
        VERSION        CHAR(50),
        LICENSE        CHAR(50),
        YEARL         INT     NOT NULL);''')
print ("Table created successfully")"""

#read data
cursor = conn.execute("SELECT ID, NAME, PHONE, ADDRESS,USERNAME, PASSWORD, SERIAL, IDS, IPS, VERSION, LICENSE, YEARL from INFORMATION")
for i in cursor :
    print (i)  
    
conn.close()


# Programming By Ali Dehghan Chaharabi
# www.alidehghanchaharabi.info