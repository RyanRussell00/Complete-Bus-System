drop database if exists CBS;
create database CBS;
use CBS;

DROP TABLE IF EXISTS EMPLOYEE;
DROP TABLE IF EXISTS ADDRESS;
DROP TABLE IF EXISTS BUS;
DROP TABLE IF EXISTS CARD;
DROP TABLE IF EXISTS TAPS;
DROP TABLE IF EXISTS FARE_TIER;
DROP TABLE IF EXISTS BUS_STOP;
DROP TABLE IF EXISTS ROUTE;
DROP TABLE IF EXISTS VISITS;
DROP TABLE IF EXISTS SCHEDULED;

CREATE TABLE EMPLOYEE (
    ssn INT(9) NOT NULL UNIQUE,
    Fname VARCHAR(15) NOT NULL,
    Minit VARCHAR(2),
    Lname VARCHAR(15) NOT NULL,
    startDate DATE,
    supervisor INT(9),
    PRIMARY KEY (ssn),
    FOREIGN KEY (supervisor)
        REFERENCES EMPLOYEE (ssn)
);

CREATE TABLE ADDRESS (
    S_ssn INT(9) NOT NULL UNIQUE,
    street VARCHAR(20) NOT NULL,
    city VARCHAR(12) NOT NULL,
    state CHAR(2) NOT NULL,
    zip CHAR(5) NOT NULL,
    PRIMARY KEY (S_ssn),
    CONSTRAINT address_ssn FOREIGN KEY (S_ssn)
        REFERENCES EMPLOYEE (ssn)
);

CREATE TABLE BUS (
    busID INT(5) NOT NULL,
    busName VARCHAR(20) NOT NULL,
    capacity INT(3) DEFAULT 1,
    manufactured_date DATE,
    E_driver INT(9) UNIQUE DEFAULT NULL,
    PRIMARY KEY (busID),
    FOREIGN KEY (E_driver)
        REFERENCES EMPLOYEE (ssn)
);
CREATE TABLE FARE_TIER (
    tier INT(2) NOT NULL,
    cost FLOAT(4 , 2 ) NOT NULL,
    fareName VARCHAR(9) DEFAULT NULL,
    PRIMARY KEY (tier)
);
CREATE TABLE CARD (
    cardNum INT(9) NOT NULL,
    balance FLOAT(4 , 2 ) DEFAULT 0,
    expiry_date DATE,
    F_fare INT(2) NOT NULL,
    PRIMARY KEY (cardNum),
    CONSTRAINT card_fare FOREIGN KEY (F_fare)
        REFERENCES FARE_TIER (tier)
);
CREATE TABLE TAPS (
    B_busID INT(5) NOT NULL,
    C_cardNum INT(9) NOT NULL,
    time_stamp DATETIME NOT NULL,
    PRIMARY KEY (B_busID , C_cardNum , time_stamp),
    CONSTRAINT tap_bus FOREIGN KEY (B_busID)
        REFERENCES BUS (busID),
    CONSTRAINT tap_card FOREIGN KEY (C_cardNum)
        REFERENCES CARD (cardNum)
);
CREATE TABLE BUS_STOP (
    stopID INT(6) NOT NULL,
    stopName VARCHAR(20) NOT NULL,
    street1 VARCHAR(20) NOT NULL,
    street2 VARCHAR(20) DEFAULT NULL,
    PRIMARY KEY (stopID)
);
CREATE TABLE ROUTE (
    routeID INT(6) NOT NULL,
    S_firstStop INT(6) NOT NULL,
    S_lastStop INT(6) NOT NULL,
    PRIMARY KEY (routeID),
    CONSTRAINT route_firstStop FOREIGN KEY (S_firstStop)
        REFERENCES BUS_STOP (stopId),
    CONSTRAINT route_lastStop FOREIGN KEY (S_lastStop)
        REFERENCES BUS_STOP (stopId)
);
CREATE TABLE VISITS (
    R_routeID INT(6) NOT NULL,
    S_stopID INT(6) NOT NULL,
    arrivalTime TIME NOT NULL,
    departTime TIME NOT NULL,
    PRIMARY KEY (R_routeID),
    CONSTRAINT visit_routeID FOREIGN KEY (R_routeID)
        REFERENCES ROUTE (routeID),
    CONSTRAINT visit_stopID FOREIGN KEY (S_stopID)
        REFERENCES BUS_STOP (stopID)
);
CREATE TABLE SCHEDULED (
    R_routeID INT(6) NOT NULL,
    B_busID INT(5),
    timeStart TIME,
    timeEnd TIME,
    PRIMARY KEY (R_routeID , B_busID),
    CONSTRAINT scheduled_routeID FOREIGN KEY (R_routeID)
        REFERENCES ROUTE (routeID),
    CONSTRAINT scheduled_busID FOREIGN KEY (B_busID)
        REFERENCES BUS (busID)
);