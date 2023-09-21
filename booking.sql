create database Destination;
use Destination;

-- creating table for South

create table South(S_N varchar(255),State varchar(255), Fav_place varchar (255), primary key(S_N));
insert into South value("S_01","TamilNadu","Ooty");
insert into South value("S_02","TamilNadu","Chennai");
insert into South value("S_03","TamilNadu","Valparai");
insert into South value("S_04","Karnataka","Murudheshwar");
insert into South value("S_05","Kerala","Wayanad");
insert into South value("S_06","Goa","Beach");
insert into South values("S_07","Kerala","Kannur");
insert into South (S_N,Fav_place) values("S_08","Valparai");
insert into South(S_N) values("S_09");
update South set State="TamilNadu" where S_N = "S_08";  
update South set State="Andhra"  where S_N= "S_09";
update South set Fav_place="Thada Falls" where S_N="S_09";

select * from South;
drop table South;
select * from South 
where State="Kerala";
select * from South
where not State="TamilNadu";

-- creating table for North

create table North(S_N varchar(255),State varchar(255),Fav_place varchar(255),Rating varchar(255),primary key(S_N));
insert into North values("N_01","Himachal Pradesh","Manali","8.7");
insert into North values("N_02","Maharashtra","Amboli","7.8");
insert into North values("N_03","Himachal Pradesh","Dalhousie","7.9");
insert into North values("N_04","Uttarakhand","Nainital","8.6");
insert into North values("N_05","Uttarakhand","Chamoli","8.0");
insert into North values("N_06","Rajasthan","Karauli","7.4");
insert into North values("N_07","Maharashtra","Lonavala","9.0");
insert into North values("N_08","Maharashtra","Ajanta","7.9");

-- creating table for booking places 
create table Booking(OTP varchar(255),Firstname varchar(255),Secondname varchar(255),To_ID varchar(255),Date_time varchar(255),primary key(OTP));
