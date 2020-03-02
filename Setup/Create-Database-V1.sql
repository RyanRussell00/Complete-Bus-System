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
DROP TABLE VISITS;
DROP TABLE SCHEDULED;

CREATE TABLE EMPLOYEE (
	ssn int(9) NOT NULL UNIQUE,
    Fname varchar(15) NOT NULL,
    Minit varchar(2),
    Lname varchar(15) NOT NULL,
    street varchar(20) NOT NULL,
    city varchar(12) NOT NULL,
    state char(2) NOT NULL,
    zip char(5) NOT NULL,
    start_date date,
    supervisor int(9),
    PRIMARY KEY (ssn),
    FOREIGN KEY (supervisor) REFERENCES EMPLOYEE(ssn)
);

CREATE TABLE BUS (
	busId int(5) not null,
    capacity int(3) default 1,
    start_date date,
    E_driver int(7) unique default null,
    PRIMARY KEY (busId),
    FOREIGN KEY (E_driver) REFERENCES EMPLOYEE(ssn)
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
	PRIMARY KEY (B_busId, C_card_num, time_stamp),
	CONSTRAINT tap_bus FOREIGN KEY (B_busId) REFERENCES BUS(busId),
	CONSTRAINT tap_card FOREIGN KEY (C_card_num) REFERENCES CARD(card_number)
);
CREATE TABLE BUS_STOP(
	stopId int(6) not null,
	stop_name varchar(20) not NULL,
	street1 varchar(20) not null,
	street2 varchar(20) default NULL,
	PRIMARY KEY (stopId),
	KEY(stop_name)
);
CREATE TABLE ROUTE(
	routeId int(6) not null,
	route_name VARCHAR(15),
	S_first_stopId int(6) not null,
	S_last_stopId int(6) not null,
	PRIMARY KEY (routeId),
	KEY(route_name),
	CONSTRAINT first_stop FOREIGN KEY (S_first_stopId) REFERENCES BUS_STOP(stopId),
	CONSTRAINT last_stop FOREIGN KEY (S_last_stopId) REFERENCES BUS_STOP(stopId)
);
CREATE TABLE VISITS(
	R_routeId int(6) not null,
	R_route_name VARCHAR(20),
	S_stopId varchar(6) not null,
	arrival_time TIME not null,
	depart_time TIME not null,
	PRIMARY KEY (R_routeId),
	CONSTRAINT visit_route_id FOREIGN KEY (R_routeId) REFERENCES BUS_STOP(stopId),
	CONSTRAINT visit_route_name FOREIGN KEY (R_route_name) REFERENCES BUS_STOP(stop_name)
);
CREATE TABLE SCHEDULED(
	R_route_id int(6) not null,
	R_route_name VARCHAR(15) NOT NULL,
    B_busId INT(5),
    time_start TIME,
    time_end TIME,
    PRIMARY KEY (R_route_id, R_route_name, B_busId, time_start),
	FOREIGN KEY (R_route_id) REFERENCES ROUTE(routeId),
	FOREIGN KEY (R_route_name) REFERENCES ROUTE(route_name),
	FOREIGN KEY (B_busId) REFERENCES BUS(busId)
);
