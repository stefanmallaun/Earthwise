
#Datenbank erzeugen (früher oder später muss der Name der Datenbank noch angepasst werden)
create database diplomarbeit collate utf16_general_ci;

#Datennbank verwenden (auch hier Namen anpassen)
use diplomarbeit;

#Datenbank löschen
#drop database diplomarbeit;

#Create quiz table
#create table quiz(
#	quizId int unsigned not null,
#    quizName varchar(100) not null,
#    discription varchar (1000) not null,
#    quiz_type varchar(100) not null,
#    neededProperties varchar(100),
#    criteria varchar(100),
#    specificCriteria varchar(100),
#    
#    constraint quizId_pk primary key (quizId)
#)engine=InnoDB;

drop table quiz;

create table quiz(
	quiz_id int unsigned not null,
    name varchar(100) not null,
    discription varchar (1000) not null,
    quiz_type varchar(100) not null,
    select_statement varchar(1000) not null,
    
    constraint quiz_id_pk primary key (quiz_id)
)engine=InnoDB;

#create country table
#create table country(
#	countryId int unsigned not null,
#    countryName varchar(100) not null,
#    continent varchar(100) not null,
    #Hier noch mehr properties 

#	constraint countryId_pk primary key (countryId)
#)engine=InnoDB;

#Version2 Create Country Table
#   name (string), official_name (string), cca2 (string), cca3 (string), independent (boolean), status (string), un_member (boolean), currencies (list), 
#   capital (list), languages (list), landlocked (boolean), area (float), population (int), timezones (list), continents (list), borders (list)

drop table country;

create table country(
	name varchar(100) not null,
    official_name varchar(100) not null,
    cca2 varchar(2) not null,
    cca3 varchar(3) not null,
    independent boolean not null,
    status varchar(100) not null,
    un_member boolean not null,
    currencies varchar(200) not null,
    capital varchar(200) not null,
    languages varchar(200) not null,
    landlocked boolean not null,
    area float not null,
    population int unsigned not null,
    timezones varchar(200) not null,
    continent varchar(20) not null,
    borders varchar(150) not null,
    
    constraint cca3_pk primary key (cca3)
)engine=InnoDB;

#create user table
create table user(
    email varchar(150) not null,
    username varchar(50) not null,
    password varchar(50) not null,

    constraint email_pk primary key (email)
)engine=InnoDB;