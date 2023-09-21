import streamlit as st
import mysql.connector
import pandas as pd
st.set_page_config(page_title='@urDesti',page_icon='https://i.etsystatic.com/15452447/r/il/d69775/1656294668/il_fullxfull.1656294668_8ou2.jpg')
choice=st.sidebar.selectbox('Menu',('Home','North','South'))
st.sidebar.image('https://www.scenicsuitcase.com/wp-content/uploads/2018/08/Types-of-Vacays-1-of-1.jpg')
st.sidebar.image("https://images.unsplash.com/photo-1515876305430-f06edab8282a?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8Y2FtcGVydmFufGVufDB8fDB8fHww&w=1000&q=80")
if(choice=='Home'):
    st.title('Welcome to @urDesti 😁')
    st.image('https://www.ibphub.com/imgs/blog/86.jpg')
    st.write('CHOOSE AND BOOK YOUR DESTINATION AT @urDesti 🧳📷😊')
elif(choice=="North"):
    st.title("Choose your destination 😁")
    st.image("https://www.rajasthantourplanner.com/blog/wp-content/uploads/2017/05/cultural-north-india.jpg")
    ch=st.selectbox("Book here",("Home","View places","Pick & Book"))
    if(ch=="Home"):
        st.image('https://indiator.com/tourist-places/wp-content/uploads/2019/01/Untitled-1.png')
    elif(ch=="View places"):
        mydb=mysql.connector.connect(host="localhost",user="root",password="abcde123",database="Destination")
        c=mydb.cursor()
        c.execute("select * from North")
        f=[]
        for i in c:
            f.append(i)
        df=pd.DataFrame(data=f,columns=c.column_names)
        st.dataframe(df)
elif(choice=="South"):
    st.title("Choose your destination 😁")
    st.image("https://www.rajasthantourplanner.com/blog/wp-content/uploads/2017/05/cultural-north-india.jpg")
    ch=st.selectbox("Book here",("Home","View places","Pick & Book"))
    if(ch=="Home"):
        st.image('https://indiator.com/tourist-places/wp-content/uploads/2019/01/Untitled-1.png')
    elif(ch=="View places"):
        mydb=mysql.connector.connect(host="localhost",user="root",password="abcde123",database="Destination")
        c=mydb.cursor()
        c.execute("select * from South")
        f=[]
        for i in c:
            f.append(i)
        df=pd.DataFrame(data=f,columns=c.column_names)
        st.dataframe(df)
elif(ch=="Pick & Book"):
    one=st.text_input("enter otp")
    two=st.text_input("enter your name")
    three=st.text_input("enter the place ID")
    four=str(datetime.datetime.now())
    bty=st.button("Book")
    if bty:
        mydb=mysql.connector.connect(host="localhost",user="root",password="abcde123",database="Destination")
        c=mydb.cursor()
        c.execute("insert into Booking values(%s,%s,%s,%s)",(one,two,three,four))
        mydb.commit()
        st.header("Booked successfully 🙌🥳")
    else:
        st.header("Sorry 😥. Please try again")

                            
