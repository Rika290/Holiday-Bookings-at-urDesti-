import streamlit as st
import mysql.connector
import pandas as pd
import datetime 
st.set_page_config(page_title='@urDesti',page_icon='https://i.etsystatic.com/15452447/r/il/d69775/1656294668/il_fullxfull.1656294668_8ou2.jpg')
choice=st.sidebar.selectbox('Dashboard',('Home','Places','Hotels'))
st.sidebar.image('https://i2.wp.com/chasingdaisiesblog.com/wp-content/uploads/2021/01/DIGITAL-peachy-dreams-picture-wall-collage-kit-peach-pink-aesthetic-travel-DIGITAL.jpeg?strip=all')
st.sidebar.image("https://images.unsplash.com/photo-1515876305430-f06edab8282a?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8Y2FtcGVydmFufGVufDB8fDB8fHww&w=1000&q=80")
if(choice=='Home'):
    st.title('Welcome to @urDesti 😁')
    st.image('https://www.ibphub.com/imgs/blog/86.jpg')
    st.write('CHOOSE AND BOOK YOUR DESTINATION AT @urDesti 🧳📷😊')
elif(choice=='Places'):
    st.image('https://www.tourism-of-india.com/pictures/tourmonth/places-to-visit-in-august-8.jpeg')
    ch2=st.selectbox('Choose',('Home','North India','South India'))
    if(ch2=="Home"):
        st.image('https://thumbs.dreamstime.com/b/travel-destination-india-map-compass-pointing-planning-42916295.jpg')
    elif(ch2=='North India'):
        st.title("Choose your destination 😁")
        ch=st.selectbox("Book here",('Home',"View places","Pick & Book"))
        if(ch=='Home'):
            st.image("https://www.rajasthantourplanner.com/blog/wp-content/uploads/2017/05/cultural-north-india.jpg")        
        elif(ch=="View places"):
            mydb=mysql.connector.connect(host="127.0.0.1",port=3306,user="root",password="abcde123",database="Destination")
            c=mydb.cursor()
            c.execute("select * from North")
            f=[]
            for i in c:
                f.append(i)
                df=pd.DataFrame(data=f,columns=c.column_names)
            st.dataframe(df)
        elif(ch=="Pick & Book"):
            st.text('You can enter the id of the chosen destination and  book')
            if 'Enter' not in st.session_state:
                st.session_state['Enter']=False
            if(not st.session_state['Enter']):
                n=st.number_input('Enter your mobile number')
                N=str(n)
                s=st.button('Enter')
                if s:
                    if len(N)==12:
                        st.session_state['Enter']=True
                        st.rerun()
                        if(not st.session_state['Enter']):
                            st.header('Please try again')
            if(st.session_state['Enter']):
                st.header('Book your place')
                mydb=mysql.connector.connect(host="127.0.0.1",port=3306,user="root",password="abcde123",database="Destination")
                c=mydb.cursor()
                c.execute("select ID,Places from North")
                f=[]
                for i in c:
                    f.append(i)
                    df=pd.DataFrame(data=f,columns=c.column_names)
                st.dataframe(df)
                one=st.text_input('Enter your 4 digit OTP here')                    
                two=st.text_input("enter your first name")
                two1=st.text_input("enter your second name")
                three=st.text_input("enter the place ID")
                fr=st.text_input("enter the Duration")
                frs=st.text_input("enter total number of members")
                five=str(datetime.datetime.now())
                bty=st.button("Book")
                if bty:
                    mydb=mysql.connector.connect(host="127.0.0.1",port=3306,user="root",password="abcde123",database="Destination")
                    c=mydb.cursor()
                    c.execute("insert into Booking values(%s,%s,%s,%s,%s,%s,%s)",(one,two,two1,three,fr,frs,five))
                    mydb.commit()                    
                    st.header("Your trip is booked successfully 🙌🥳 \nA message is sent to the given mobile number  regarding transport and other details. \nHave a Happy & Safe Vacation🤗")   
    elif(ch2=='South India'):
        st.title("Choose your destination 😁")
        ch=st.selectbox("Book here",('Home',"View places","Pick & Book"))
        if(ch=='Home'):
            st.image('https://www.sikhheros.com/wp-content/uploads/2022/12/Best-Places-to-Visit-in-South-India-This-December.png')        
        elif(ch=="View places"):
            mydb=mysql.connector.connect(host="127.0.0.1",port=3306,user="root",password="abcde123",database="Destination")
            c=mydb.cursor()
            c.execute("select * from South")
            f=[]
            for i in c:
                f.append(i)
                df=pd.DataFrame(data=f,columns=c.column_names)
            st.dataframe(df)
        elif(ch=="Pick & Book"):            
            if 'Enter' not in st.session_state:
                st.session_state['Enter']=False
            if(not st.session_state['Enter']):
                n=st.number_input('Enter your mobile number')
                N=str(n)
                s=st.button('Enter')
                if s:
                    if len(N)==12:
                        st.session_state['Enter']=True
                        st.rerun()
                        if(not st.session_state['Enter']):
                            st.header('Please try again')
            if(st.session_state['Enter']):
                st.header('Book your place')
                mydb=mysql.connector.connect(host="127.0.0.1",port=3306,user="root",password="abcde123",database="Destination")
                c=mydb.cursor()
                c.execute("select ID,Places from South")
                f=[]
                for i in c:
                    f.append(i)
                    df=pd.DataFrame(data=f,columns=c.column_names)
                st.dataframe(df)
                one=st.text_input('Enter your 4 digit OTP here')                    
                two=st.text_input("enter your first name")
                two1=st.text_input("enter your second name")
                three=st.text_input("enter the place ID")
                fr=st.text_input("enter the Duration")
                frs=st.text_input("enter total number of members")
                five=str(datetime.datetime.now())
                bty=st.button("Book")
                if bty:
                    mydb=mysql.connector.connect(host="127.0.0.1",port=3306,user="root",password="abcde123",database="Destination")
                    c=mydb.cursor()
                    c.execute("insert into Booking values(%s,%s,%s,%s,%s,%s,%s)",(one,two,two1,three,fr,frs,five))
                    mydb.commit()                    
                    st.header("Your trip is booked successfully 🙌🥳 \nA message is sent to the given mobile number  regarding transport and other details. \nHave a Happy & Safe Vacation🤗")
elif(choice=='Hotels'):
    st.image('https://drop.ndtv.com/albums/BUSINESS/sahara_subrata/slide1_collage.jpg')
    ch=st.selectbox('Menu',('Home','North','South'))
    if(ch=='Home'):
        st.text('We provide you a list of hotels which are rated as 3 and above. \nBook fast and enjoy your vacation😊')
        st.image('https://media.istockphoto.com/id/456859205/photo/multiple-photographs-of-vacation-scenes.jpg?s=612x612&w=0&k=20&c=fX2gODiFol1sbYDwPJ5LqC_QeABp2ibs8I4DQp0q8Lo=')
    elif(ch=='North'):
        mydb=mysql.connector.connect(host="127.0.0.1",port=3306,user="root",password="abcde123",database="Destination")
        c=mydb.cursor()
        c.execute("select distinct(places) from north order by (1)")
        f=[]
        for i in c:
            f.append(i)
            df=pd.DataFrame(data=f,columns=c.column_names)
        st.dataframe(df)
        hot=st.text_input('You can choose your hotel/resort')
        ht=st.button('Check')
        if ht:
            db=mysql.connector.connect(host="127.0.0.1",port=3306,user="root",password="abcde123",database="Destination")
            m=db.cursor()
            m.execute("select * from hotels where places= %s",(hot,))
            g=[]
            flag=True
            for j in m:
                if(j[2]==hot):
                    g.append(j)
                    di=pd.DataFrame(data=g,columns=m.column_names)
                    flag=False
            if flag:
                st.header("Sorry😢 \n No Hotel/Resort available for the chosen place")                    
            else:
                st.dataframe(di)
                st.header("🥳 \n Kindly visit their websites for booking and other details")
    else:
        mydb=mysql.connector.connect(host="127.0.0.1",port=3306,user="root",password="abcde123",database="Destination")
        c=mydb.cursor()
        c.execute("select distinct(places) from south order by (1)")
        f=[]
        for i in c:
            f.append(i)
            df=pd.DataFrame(data=f,columns=c.column_names)
        st.dataframe(df)
        hot=st.text_input('You can choose your hotel/resort')
        ht=st.button('Check')
        if ht:
            db=mysql.connector.connect(host="127.0.0.1",port=3306,user="root",password="abcde123",database="Destination")
            m=db.cursor()
            m.execute("select * from hotels where places= %s",(hot,))
            g=[]
            flag=True
            for j in m:
                if(j[2]==hot):
                    g.append(j)
                    di=pd.DataFrame(data=g,columns=m.column_names)
                    flag=False
            if flag:
                st.header("Sorry😢 \n No Hotel/Resort available for the chosen place")                    
            else:
                st.dataframe(di)
                st.header("🥳 \n Kindly visit their websites for booking and other details")
        
                
                
            
                
                
               

                          

