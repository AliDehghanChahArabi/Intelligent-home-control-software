import sqlite3

conn = sqlite3.connect('smarthome.db')

"""conn.execute('''CREATE TABLE MANUALCTRL
       (ID INT PRIMARY KEY     NOT NULL,
        R1           INT    NOT NULL,
        R2           INT    NOT NULL,
        R3           INT    NOT NULL,
        R4           INT    NOT NULL,
        R5           INT    NOT NULL,
        R6           INT    NOT NULL);''')
print ("Table created successfully")"""

#import Data
conn.execute("INSERT INTO MANUALCTRL (ID,R1,R2,R3,R4,R5,R6) \
      VALUES (1,0,0,1,1,0,0)");

conn.commit()
conn.close()



# Programming By Ali Dehghan Chaharabi
# www.alidehghanchaharabi.info