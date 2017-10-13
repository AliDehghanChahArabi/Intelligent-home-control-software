import sqlite3

conn = sqlite3.connect('smarthome.db')

"""conn.execute('''CREATE TABLE RESOLUTION
       (ID INT PRIMARY KEY     NOT NULL,
        nST1           INT    NOT NULL,
        MST1           INT    NOT NULL,
        nST2           INT    NOT NULL,
        MST2           INT    NOT NULL,
        nST3           INT    NOT NULL,
        MST3           INT    NOT NULL,
        nST4           INT    NOT NULL,
        MST4           INT    NOT NULL,
        nSL1           INT    NOT NULL,
        MSL1           INT    NOT NULL,
        nSL2           INT    NOT NULL,
        MSL2           INT    NOT NULL,
        nSL3           INT    NOT NULL,
        MSL3           INT    NOT NULL,
        nSL4           INT    NOT NULL,
        MSL4           INT    NOT NULL,
        nSW1           INT    NOT NULL,
        MSW1           INT    NOT NULL,
        nSW2           INT    NOT NULL,
        MSW2           INT    NOT NULL,
        nSW3           INT    NOT NULL,
        MSW3           INT    NOT NULL,
        nSW4           INT    NOT NULL,
        MSW4           INT    NOT NULL,
        nSD1           INT    NOT NULL,
        MSD1           INT    NOT NULL,
        nSD2           INT    NOT NULL,
        MSD2           INT    NOT NULL,
        nSD3           INT    NOT NULL,
        MSD3           INT    NOT NULL,
        nSD4           INT    NOT NULL,
        MSD4           INT    NOT NULL);''')
print ("Table created successfully")"""

#import Data
conn.execute("INSERT INTO RESOLUTION (ID,nST1,MST1,nST2,MST2,nST3,MST3,nST4,MST4,nSL1,MSL1,nSL2,MSL2,nSL3,MSL3,nSL4,MSL4,nSW1,MSW1,nSW2,MSW2,nSW3,MSW3,nSW4,MSW4,nSD1,MSD1,nSD2,MSD2,nSD3,MSD3,nSD4,MSD4) \
      VALUES (2, 2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33)");

conn.commit()
conn.close()



# Programming By Ali Dehghan Chaharabi
# www.alidehghanchaharabi.info
