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

#import data

conn.execute("INSERT INTO INFORMATION(ID, NAME, PHONE, ADDRESS,USERNAME, PASSWORD, SERIAL, IDS, IPS, VERSION, LICENSE, YEARL)\
      VALUES (1, 'Ali Dehghan Chaharabi', 09120883990, 'Tehran - Iran', 'alidehghan', 'nahghedila', 'ipmm123456adch', '1234AD', '192.168.1.1', '1.0.0', 'iPMM Co.', 1)");

conn.commit()
conn.close()
print ("import ok")


# Programming By Ali Dehghan Chaharabi
# www.alidehghanchaharabi.info