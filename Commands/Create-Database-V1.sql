-- CREATE TABLE ADDRESS(
-- STREET varchar(20) not null,
-- CITY varchar (12) not null,
-- STATE char(2) not null,
-- ZIP char(5) not null,
-- primary key(STREET, CITY, STATE, ZIP)
-- );
-- 
-- CREATE TABLE FULL_NAME(
-- FIRST_NAME varchar(15),
-- MIDDLE_INITIAL char(2),
-- LAST_NAME varchar(15),
-- primary key (FIRST_NAME, MIDDLE_INITIAL, LAST_NAME)
-- );

CREATE TABLE EMPLOYEE(
ID	int(7) not null unique auto_increment,
F_NAME varchar(40) not null,
SSN int(9) not null unique,
A_ADDRESS varchar(100) not null,
START_DATE date,
SUPERVISOR int(7),
primary key(id)
-- constraint Name_Constraint foreign key (F_NAME) references FULL_NAME(FIRST_NAME, MIDDLE_INITIAL, LAST_NAME),
-- constraint Address_Constraint foreign key (A_ADDRESS) references ADDRESS(STREET, CITY, STATE, ZIP)
);
