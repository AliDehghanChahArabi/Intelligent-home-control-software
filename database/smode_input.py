import sqlite3

conn = sqlite3.connect('smarthome.db')

#Tabel
"""conn.execute('''CREATE TABLE SYSTEMMODE
       (ID INT PRIMARY KEY     NOT NULL,
        mode           INT    NOT NULL,
        date            TEXT     NOT NULL);''')
print ("Table created successfully")"""

#import data

conn.execute("INSERT INTO SYSTEMMODE(ID, mode, date)\
      VALUES (1, 1, '11/11/11' )");

conn.commit()
conn.close()
print ("import ok")


# Programming By Ali Dehghan Chaharabi
# www.alidehghanchaharabi.info