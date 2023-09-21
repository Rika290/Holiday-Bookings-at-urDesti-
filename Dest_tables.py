import mysql.connector
import pandas as pd
db=mysql.connector.connect(host="localhost",user="root",password="abcde123",database="Destination")
c=db.cursor()
'''
c.execute("select * from South")
l=[]
for i in c:
    l.append(i)
df=pd.DataFrame(data=l,columns=c.column_names)
print(df)
'''
'''
c.execute("select * from North")
l=[]
for i in c:
    l.append(i)
df=pd.DataFrame(data=l,columns=c.column_names)
print(df)
'''
'''
c.execute("select * from Booking")
l=[]
for i in c:
    l.append(i)
df=pd.DataFrame(data=l,columns=c.column_names)
print(df)
'''
c.execute("select * from hills")
l=[]
for i in c:
    l.append(i)
df=pd.DataFrame(data=l,columns=c.column_names)
print(df)
