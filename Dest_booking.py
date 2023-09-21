import mysql.connector
import datetime
import pandas as pd
mydb=mysql.connector.connect(host="localhost",user="root",password="abcde123",database="Destination")
print(mydb)
c=mydb.cursor()
c.execute("select * from Booking")
m=[]
for i in c:
    m.append(i)
df=pd.DataFrame(data=m,columns=c.column_names)
print(df)
