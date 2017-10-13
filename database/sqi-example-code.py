
import sqlite3

conn = sqlite3.connect('smarthome.db')
print ("Opened database successfully")

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

"""conn.execute('''CREATE TABLE SMARTCTRL
       (ID INT PRIMARY KEY     NOT NULL,
        SCSR1A           INT    NOT NULL,
        SCSR1B           INT    NOT NULL,
        SCSR2A           INT    NOT NULL,
        SCSR2B           INT    NOT NULL,
        SCSR3A           INT    NOT NULL,
        SCSR3B           INT    NOT NULL,
        SCSR4A           INT    NOT NULL,
        SCSR4B           INT    NOT NULL,
        SCSR5A           INT    NOT NULL,
        SCSR5B           INT    NOT NULL,
        SCSR6A           INT    NOT NULL,
        SCSR6B           INT    NOT NULL,
        SCTR1A           INT    NOT NULL,
        SCTR1B           INT    NOT NULL,
        SCTR1C           INT    NOT NULL,
        SCTR1D           INT    NOT NULL,
        SCTR2A           INT    NOT NULL,
        SCTR2B           INT    NOT NULL,
        SCTR2C           INT    NOT NULL,
        SCTR2D           INT    NOT NULL,
        SCTR3A           INT    NOT NULL,
        SCTR3B           INT    NOT NULL,
        SCTR3C           INT    NOT NULL,
        SCTR3D           INT    NOT NULL,
        SCTR4A           INT    NOT NULL,
        SCTR4B           INT    NOT NULL,
        SCTR4C           INT    NOT NULL,
        SCTR4D           INT    NOT NULL,
        SCTR5A           INT    NOT NULL,
        SCTR5B           INT    NOT NULL,
        SCTR5C           INT    NOT NULL,
        SCTR5D           INT    NOT NULL,
        SCTR6A           INT    NOT NULL,
        SCTR6B           INT    NOT NULL,
        SCTR6C           INT    NOT NULL,
        SCTR6D           INT    NOT NULL);''')
print ("Table created successfully")"""

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
"""conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (1, 'Paul', 32, 'California', 20000.00 )");

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");

conn.commit()
print ("Records created successfully")"""

#read Data
"""cursor = conn.execute("SELECT id, name, address, salary  from COMPANY")
for row in cursor:
   print ("ID = ", row[0])
   print ("NAME = ", row[1])
   print ("ADDRESS = ", row[2])
   print ("SALARY = ", row[3], "\n")

print ("Operation done successfully")"""

#update Data
"""conn.execute("UPDATE COMPANY set SALARY = 25000.00 where ID=1")
conn.commit
print ("Total number of rows updated :", conn.total_changes)

cursor = conn.execute("SELECT id, name, address, salary  from COMPANY")
for row in cursor:
   print ("ID = ", row[0])
   print ("NAME = ", row[1])
   print ("ADDRESS = ", row[2])
   print ("SALARY = ", row[3], "\n")

print ("Operation done successfully")"""

#delet Data
"""conn.execute("DELETE from COMPANY where ID=2;")
conn.commit
print ("Total number of rows deleted :", conn.total_changes)

cursor = conn.execute("SELECT id, name, address, salary  from COMPANY")
for row in cursor:
   print ("ID = ", row[0])
   print ("NAME = ", row[1])
   print ("ADDRESS = ", row[2])
   print ("SALARY = ", row[3], "\n")

print ("Operation done successfully")"""



conn.close()


# Programming By Ali Dehghan Chaharabi
# www.alidehghanchaharabi.info