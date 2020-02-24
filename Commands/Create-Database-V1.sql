-- CREATE TABLE EMPLOYEE (
--     ID INT(7) NOT NULL UNIQUE AUTO_INCREMENT,
--     FIRST_NAME VARCHAR(15) NOT NULL,
--     MID_INIT VARCHAR(2),
--     LAST_NAME VARCHAR(15) NOT NULL,
--     STREET VARCHAR(20) NOT NULL,
--     CITY VARCHAR(12) NOT NULL,
--     STATE CHAR(2) NOT NULL,
--     ZIP CHAR(5) NOT NULL,
--     SSN INT(9) NOT NULL UNIQUE,
--     START_DATE DATE,
--     SUPERVISOR INT(7),
--     PRIMARY KEY (ID),
--     KEY (SSN)
-- );

CREATE TABLE BUS(
	ID int(5) not null,
    CAPACITY int(3) default 1,
    START_DATE date,
    DRIVER int(7) unique default null,
    primary key (ID),
    foreign key (DRIVER) references EMPLOYEE (ID)
);