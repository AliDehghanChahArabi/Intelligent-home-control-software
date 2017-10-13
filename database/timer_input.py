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

#import data

conn.execute("INSERT INTO TIMER(ID, T1,T2,T3,T4,T5,T6)\
      VALUES (5, '00,00,00,00', '11,11,11,11', '22,22,22,22', '11,33,11,33', '11,44,11,44', '11,55,11,55')");

conn.commit()
conn.close()
print ("import ok")


# Programming By Ali Dehghan Chaharabi
# www.alidehghanchaharabi.info