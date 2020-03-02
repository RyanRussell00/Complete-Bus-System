drop database CBS;
create database CBS;
use CBS;

DROP TABLE EMPLOYEE;
DROP TABLE BUS;
DROP TABLE CARD;
DROP TABLE TAPS;
DROP TABLE FARE_TIER;
DROP TABLE BUS_STOP;
DROP TABLE ROUTE;
DROP TABLE VISIT;
DROP TABLE SCHEDULED;

CREATE TABLE EMPLOYEE (
	ssn int(9) NOT NULL UNIQUE,
    Fname varchar(15) NOT NULL,
    Minit varchar(2),
    Lname varchar(15) NOT NULL,
    street varcharR(20) NOT NULL,
    city varchar(12) NOT NULL,
    state char(2) NOT NULL,
    zip char(5) NOT NULL,
    start_date date,
    supervisor int(7),
    PRIMARY KEY (id),
    KEY (ssn)
);

CREATE TABLE BUS (
	busId int(5) not null,
    capacity int(3) default 1,
    start_date date,
    E_driver int(7) unique default null,
    PRIMARY KEY (id),
    FOREIGN KEY (driver) REFERENCES EMPLOYEE(id)
);
CREATE TABLE FARE_TIER (
	tier int(2) not null,
	cost float(4, 2) not null,
	fare_name varchar(9) default NULL,
	PRIMARY KEY (tier)
);
CREATE TABLE CARD (
	card_number int(9) not null,
	balance float(4, 2) default 0,
	expiry_date DATE,
	F_fare int(2) not null, 
	PRIMARY KEY (card_number),
	CONSTRAINT card_fare FOREIGN KEY (F_fare) REFERENCES FARE_TIER(tier)
);
CREATE TABLE TAPS (
	B_busId int(5) not null,
	C_card_num int(9) not null,
	time_stamp DATETIME not null,
	PRIMARY KEY (bus_id, card_num, time_stamp)
	CONSTRAINT tap_bus FOREIGN KEY (B_busId) REFERENCES BUS(id);
	CONSTRAINT tap_card FOREIGN KEY (C_card_num) REFERENCES CARD(card_number);
);
CREATE TABLE BUS_STOP(
	stopId int(6) not null,
	stop_name varchar(20) default NULL,
	street1 varchar(20) not null,
	street2 varchar(20) default NULL,
	PRIMARY KEY (stopId)
);
CREATE TABLE ROUTE(
	routeId int(6) not null,
	route_name VARCHAR(15),
	S_first_stopId varchar(6) not null,
	S_last_stopId varchar(6) not null,
	PRIMARY KEY (routeId),
	#ToDo: Do these constraints need to be here? What happens when you delete a Route or Stop Id??
	CONSTRAINT firstStop FOREIGN KEY first_stopId REFERENCES BUS_STOP(stopId),
	CONSTRAINT firstStop FOREIGN KEY last_stopId REFERENCES BUS_STOP(stopId)
);
CREATE TABLE VISITS(
	R_routeId int(6) not null,
	R_route_name VARCHAR(15),
	S_stopId varchar(6) not null,
	arrival_time TIME not null,
	depart_time TIME not null,
	PRIMARY KEY (routeId),
	#ToDo: Do these constraints need to be here? What happens when you delete a Route or Stop Id??
	CONSTRAINT firstStop FOREIGN KEY first_stopId REFERENCES BUS_STOP(stopId),
	CONSTRAINT firstStop FOREIGN KEY last_stopId REFERENCES BUS_STOP(stopId)
);
CREATE TABLE SCHEDULED(
	R_route_id int(6) not null,
	R_route_name VARCHAR(15) NOT NULL,
    B_busId INT(5),
    time_start TIME,
    time_end TIME,
    PRIMARY KEY (R_route_id, R_route_name, B_busId, time_start),
	FOREIGN KEY (R_route_id) REFERENCES ROUTE(routeId,
	FOREIGN KEY (R_route_name) REFERENCES ROUTE(route_name),
	FOREIGN KEY (B_busId) REFERENCES BUS(busId)
);