import sqlite3

conn = sqlite3.connect('smarthome.db')

#Tabel
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

#read data
cursor = conn.execute("SELECT ID,SCSR1A,SCSR1B,SCSR2A,SCSR2B,SCSR3A,SCSR3B,SCSR4A,SCSR4B,SCSR5A,SCSR5B,SCSR6A,SCSR6B,SCTR1A,SCTR1B,SCTR1C,SCTR1D,SCTR2A,SCTR2B,SCTR2C,SCTR2D,SCTR3A,SCTR3B,SCTR3C,SCTR3D,SCTR4A,SCTR4B,SCTR4C,SCTR4D,SCTR5A,SCTR5B,SCTR5C,SCTR5D,SCTR6A,SCTR6B,SCTR6C,SCTR6D from SMARTCTRL")
for i in cursor :
    print (i)  
    
conn.close()


# Programming By Ali Dehghan Chaharabi
# www.alidehghanchaharabi.info