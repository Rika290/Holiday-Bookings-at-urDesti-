-- database called destination is used
use destination; 

-- table for storing places in north is created

create table North(ID varchar(255),State_UT varchar(255),Places varchar(255),primary key(ID));
-- inserting values to the table

insert into North values("N_01","Himachal Pradesh","Manali"),("N_02","Maharashtra","Amboli"),("N_03","Himachal Pradesh","Dalhousie"),
("N_04","Uttarakhand","Nainital"),("N_05","Uttarakhand","Chamoli"),("N_06","Rajasthan","Karauli"),
("N_07","Maharashtra","Lonavala"),("N_08","Maharashtra","Ajanta"),('N_09','Maharashtra','Igatpuri'),
('N_10','Himachal Pradesh','Kasauli'),('N_11','Himachal Pradesh','Bir'),('N_12','Uttarakhand','Rishikesh'),
('N_13','Uttarakhand', 'Mussoorie'),('N_14','Himachal Pradesh','Kufri'),('N_15','Jammu and Kashmir','Gulmarg'),('N_16','Punjab','Amritsar'),
('N_17','Ladakh','Leh'),('N_18','Uttar Pradesh','Sarnath'),('N_19','Haryana','Jyotisar'),('N_20','Himachal Pradesh','Spiti'),('N_21','Uttar Pradesh','Agra'),
('N_22','Madhya Pradesh','Gwalior'),('N_23','Maharashtra','Satara'),('N_24','Madhya Pradesh','Pachmarhi'),('N_25','Jammu and Kashmir','Pahalgam');

-- displaying all values from the table north
select * from north;

-- Table named South is created for storing places in South India
create table South(ID varchar(255),State_UT text,Places text,primary key(ID));

-- inserting values to the table
insert into South value("S_01","TamilNadu","Ooty"),("S_02",'Goa','Vanxim'),("S_03","TamilNadu","Valparai"),("S_04","Karnataka","Murudheshwar"),
("S_05","Kerala","Wayanad"),("S_06",'Karnataka','Hampi'),("S_07","Kerala","Kannur"),("S_08","Andhra","Nallamala Hills"),("S_09","Kerala","Munnar"),
("S_10",'Andhra','Lambasingi'),('S_11','TamilNadu','Megamalai'),('S_12','Karnataka',"St. Mary's Islands"),('S_13','Karnataka','Gokarna'),
('S_14','Andhra','Araku Valley'),('S_15','Andhra','Ahobilam'),('S_16','Kerala','Idukki'),('S_17','Tamil Nadu','Kolukkumalai'),('S_18','Goa','Divar Island'),
('S_19','Tamil Nadu','Pamban Island'),('S_20','Kerala','Ponmudi'),('S_21','Andaman and Nicobar','Havelock Island'),('S_22',' Puducherry','Mahe'),
('S_23','Tamil Nadu','Kodaikanal'),('S_24','Lakshadweep','Kalpeni'),('S_25','Lakshadweep','Kavaratti');

-- displaying all values from the table south
select * from south;

-- A table named hotels is created 
create table Hotels(S_No numeric,Name varchar(255),Places text, Category varchar(255),primary key(S_No));

-- inserting values into the hotels table
insert into Hotels values(1,'Fortune Resort Sullivan Court','Ooty','3-star'),(2,'Sterling Ooty - Fern Hill','Ooty','5-star hotel'),
(3,'Valparai Mount Terrain Resort','Valparai','3-star hotel'),(4,'Hotel Hampi International','Hampi','3-star hotel'),
(5,'The Fern Kadamba Hotel','Goa','5-star hotel'),(6,'Silvergreen Resort','Wayanad','3-star hotel'),
(7,'Heritage Resort','Hampi','4-star hotel'),(8,'Mascot Beach Resort','Kannur','3-star hotel'),(9,'RNS Residency','Murdeshwar','4-star hotel'),
(10,'Club Mahindra White Meadows','Manali','5-star hotel'),(11,'Alps Resort Dalhousie','Dalhousie','3-star hotel'),
(12,'Hotel Spiti Heritage','Spiti','3-star hotel'),(13,'The Vintage Gulmarg','Gulmarg','4-star hotel'),(14,'Tulip Inn Green Castle','Mussoorie','4-star hotel'),
(15,'The Autumn Home','Bir','3 star Homestay'),(16,'Banon Resorts','Manali','3-star hotel'),(17,'The Cliff Resort','Munnar','3-star hotel')
,(18,'Tea County','Munnar','4-star hotel'),(19,'Ocean Breeze Cottage','Gokarna','3-star cottage'),(20,'Hilltop Mrugavani','Nallamala Hills','3-star Resort'),
(21,'Cotsvilla Resort','Valparai','4-star Resort'),(22,'Aventura','Ooty','4-star hotel'),(23,'Bhanwar Vilas Palace','Karauli','3-star hotel'),
(24,'Whispering Woods Resort','Lonavala','3-star hotel'),(25,'Club Mahindra White Meadows','Manali','5-star hotel'),
(26,'Aloha On The Ganges','Rishikesh','3-star hotel'),(27,'Jungle Beats Resorts','Wayanad','3-star hotel'),(28,'Paradise Isle Beach Resort',"St. Mary's Islands",
'3-star hotel'),(29,'Tulsi Village Retreat','Idukki','3-star hotel'),(30,'KTDC Golden Peak Ponmudi','Ponmudi','3-star hotel'),(31,'Oxygen Resorts','Idukki',
'4-star hotel'),(32,'Casa Holiday Resorts','Araku Valley','4-star hotel'),(33,'The Residency Towers Rameswaram','Pamban Island','4-star hotel'),
(34,'Savoy','Ooty','5-star hotel'),(35,'The Wind','Kolukkumalai','3-star hotel'),(36,'MTDC Guest House','Ajanta','3-star hotel'),(37,'Hotel Lake And Woods',
'Nainital','3-star hotel'),(38,'Green Hill Resort','Amboli','3-star hotel'),(39,'The Lagoona Resort','Lonavala','4-star hotel'),(40,'Regenta Place','Amritsar',
'4-star hotel'),(41,'Royal Orchid Fort Resort','Mussoorie','4-star hotel'),(42,'Misty Lake Resorts','Idukki','3-star hotel'),(43,'Hotel HillView','Munnar',
'3-star hotel'),(44,'Welcome Hotel','Gulmarg','3-star hotel'),(45,'JK Clarks Exotica','Dalhousie','4-star hotel'),
(46,'Sterling Kodai Lake','Kodaikanal','5-star hotel'),(47,'Hotel RT Hill View','Kodaikanal','3-star hotel'),(48,'Bangaram Island Resort',
'Kalpeni','2-star hotel'),(49,'Havelock country homes','Havelock Island','3-star hotel'),(50,'SilverSand Village Resort','Havelock Island','4-star hotel');

-- displaying all values of the table
select * from Hotels;

-- A table named Booking is created which stores detail of customers
create table Booking(OTP varchar(255),Firstname varchar(255),Secondname varchar(255),Place_ID varchar(255),Duration varchar(255),Total_Members numeric,
Date_time varchar(255),primary key(OTP));
-- displaying all values of the table
select * from Booking;
