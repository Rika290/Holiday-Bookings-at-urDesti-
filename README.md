# Holiday Bookings at "@urDesti😁"

 - People love to travel and explore new places. To have a happy and safe vacation, many travel agencies are available.
 - For the same purpose, a Web App for a fictitious  travel agency called @urDesti😁 which provides vacation plans in India  is created.
 - It is a Graphical User Interface(GUI) based application developed with the help of Python programming language and MySQL RDBMS.

Data used:
  1) Destination tables:
 - In the MySQL Workbench, tables called North and South were created
 - Entries like States(of North India,South India), famous tourist places in theose States, along with a ID number were added
 -  In this case, the ID numbers created are unique and hence made as the primary key of both tables
 
 2) Table for Hotels/Resorts
- A table called Hotels was created
- Entries like S.No,Name,Places were added
- Here, the column S.No has only unique values  and therefore is the primary key

3) Table for Booking
- A table which gets info from customers for reservation of rooms and travel
- Details like OTP,name of the customer are included
- Since OTP is unique, it is considered as the primary key
 
Features integrated:
  - This app is for booking transport to different tourist places in North and South India
  - A list of places are provided, which customers can view and book the transport
  - For accomodation, information on available hotels in those places are displayed
  - By entering a unique OTP number the user is able to login and view the details
  - The user can choose and book his/her destination and hotel (if available).

Tools used:
 1) This app is developed by fully utilizing the Python programming language
   -  Pandas the Python library is used for viewing the data in form of data frames
   -  Streamlit, an open source framework under Python is used as an interface to create this web application
 2) MySQL, an open-source Relational Database Management System (RDBMS) is used for generating the data.

    

