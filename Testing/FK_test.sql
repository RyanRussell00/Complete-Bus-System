-- Tests all the foreign key constraints

-- PHIL'S TESTS

-- TEST: employee supervisor goes back to employee ssn
DELETE FROM EMPLOYEE;
INSERT INTO EMPLOYEE (ssn, Fname, Minit, Lname, startDate, supervisor)
VALUES (111111111, 'Super', 'V', 'Isor', '2019-01-01', NULL);
INSERT INTO ADDRESS (S_ssn, street, city, state, zip) 
VALUES (111111111, '123 1st Street', 'Redmond', 'WA', '98052');

INSERT INTO EMPLOYEE (ssn, Fname, Minit, Lname, startDate, supervisor)
VALUES (222222222, 'Subo', 'R', 'Dinate', '2020-02-01', 111111111);
INSERT INTO ADDRESS (S_ssn, street, city, state, zip) 
VALUES (222222222, '456 2nd Street', 'Redmond', 'WA', '98052');
	-- a manager and their subordinate, linked by an FK

SELECT ssn, supervisor
FROM EMPLOYEE;
	-- should show two employees, one managing the other

DELETE FROM EMPLOYEE
WHERE ssn = 111111111;
	-- removing the supervisor should not affect the subordinate employee
	-- perhaps the 'Subo' employee's supervisor attribute should change to NULL too?
	-- CURRENT BEHAVIOR: fails because manager ssn is a foreign key in another employee

SELECT ssn, supervisor
FROM EMPLOYEE;
	-- CURRENT BEHAVIOR: still shows the two employees

UPDATE EMPLOYEE
SET supervisor = NULL
WHERE ssn = 222222222;
	-- remove the manager's key from the subordinate employee

DELETE FROM EMPLOYEE
WHERE ssn = 111111111;
	-- try deleting the manager again

SELECT ssn, supervisor
FROM EMPLOYEE;
	-- only 1 employee should remain: the original subordinate

DELETE FROM EMPLOYEE;


-- TEST: bus E_driver goes back to employee ssn
DELETE FROM BUS;
DELETE FROM EMPLOYEE;

INSERT INTO EMPLOYEE (ssn, Fname, Minit, Lname, startDate, supervisor)
VALUES (111111111, 'Bus', 'D', 'River','2020-01-01', NULL);
INSERT INTO ADDRESS (S_ssn, street, city, state, zip) 
VALUES (111111111, '123 1st Street', 'Redmond', 'WA', '98052');

INSERT INTO BUS (busID, busName, capacity, manufactured_date, E_driver)
VALUES (11111, '535 Lynnwood', 20, NULL, 111111111);
	-- an employee and a bus, linked by an FK because the employee drives the bus

DELETE FROM EMPLOYEE
WHERE ssn = 111111111;
	-- try deleting the driver
	-- CURRENT BEHAVIOR: fails because employee has a foreign key in the bus

SELECT ssn
FROM EMPLOYEE;

SELECT busID, E_driver
FROM BUS;
	-- original bus and employee remain

UPDATE BUS
SET E_driver = NULL
WHERE busID = 11111;
	-- remove driver employee's key from the bus

DELETE FROM EMPLOYEE
WHERE ssn = 111111111;
	-- try deleting the driver again

SELECT ssn
FROM EMPLOYEE;

SELECT busID, E_driver
FROM BUS;
	-- no employees should remain
	-- bus should be driverless

DELETE FROM BUS;

-- taps B_busId goes back to bus busId
DELETE FROM TAPS;
DELETE FROM CARD;
DELETE FROM FARE_TIER;
DELETE FROM BUS;

INSERT INTO BUS (busID, busName, capacity, manufactured_date, E_driver)
VALUES (11111, '535 Lynnwood', 60, '2020-01-01', NULL);

INSERT INTO FARE_TIER (tier, cost, fareName)
VALUES (01, 2.50, NULL);

INSERT INTO CARD (cardNum, balance, expiry_date, F_fare)
VALUES (111111111, 25.00, '2020-12-01', 01);

INSERT INTO TAPS (B_busID, C_cardNum, time_stamp)
VALUES (11111, 111111111, '2020-03-01 10:00:00');
	-- bare minimum records for a taps and bus relationship

DELETE FROM BUS
WHERE busID = 11111;
	-- try deleting the bus
	-- CURRENT BEHAVIOR: fails by FK constraint to taps

SELECT busID
FROM BUS;

SELECT B_busID, C_cardNum, time_stamp
FROM TAPS;
	-- shows a bus and a tap record

DELETE FROM TAPS
WHERE B_busID = 11111;
	-- remove tap records

SELECT busID
FROM BUS;

SELECT B_busID, C_cardNum, time_stamp
FROM TAPS;
	-- should show a bus and no tap record
	
DELETE FROM TAPS;
DELETE FROM BUS;

-- taps C_card_num goes back to card cardNum
DELETE FROM TAPS;
DELETE FROM BUS;
DELETE FROM CARD;
DELETE FROM FARE_TIER;

INSERT INTO FARE_TIER (tier, cost, fareName)
VALUES (01, 2.50, NULL);

INSERT INTO CARD (cardNum, balance, expiry_date, F_fare)
VALUES (111111111, 25.00, '2020-12-01', 01);

INSERT INTO BUS (busID, busName, capacity, manufactured_date, E_driver)
VALUES (11111, '535 Lynnwood', 20, NULL, NULL);

INSERT INTO TAPS (B_busID, C_cardNum, time_stamp)
VALUES (11111, 111111111, '2020-03-01 10:00:00');
	-- bare minimum for a taps and card relationship

DELETE FROM CARD
WHERE cardNum = 111111111;
	-- try deleting a card
	-- CURRENT BEHAVIOR: fails by FK constraint to taps

SELECT cardNum
FROM CARD;

SELECT B_busID, C_cardNum, time_stamp
FROM TAPS;
	-- shows a card and a tap record

DELETE FROM TAPS
WHERE C_cardNum = 111111111;
	-- remove tap record

SELECT cardNum
FROM CARD;

SELECT B_busID, C_cardNum, time_stamp
FROM TAPS;
	-- should show a card but no tap records

DELETE FROM TAPS;
DELETE FROM CARD;

-- card F_fare goes back to faretier tier
DELETE FROM CARD;
DELETE FROM FARE_TIER;

INSERT INTO FARE_TIER (tier, cost, fareName)
VALUES (01, 2.50, NULL);

INSERT INTO CARD (cardNum, balance, expiry_date, F_fare)
VALUES (111111111, 25.00, '2020-12-01', 01);
	-- create a card connected to a fare tier

DELETE FROM FARE_TIER
WHERE tier = 01;
	-- try removing the fare tier
	-- CURRENT BEHAVIOR: fails because of an FK constraint to card

SELECT tier
FROM FARE_TIER;

SELECT cardNum
FROM CARD;
	-- shows a fare tier and a card with that tier

DELETE FROM CARD
WHERE cardNum = 111111111;
	-- remove the card

SELECT tier
FROM FARE_TIER;

SELECT cardNum
FROM CARD;
	-- should show a fare tier but not card

DELETE FROM CARD;
DELETE FROM FARE_TIER;

-- visits R_routeId goes back to route routeId
DELETE FROM VISITS;
DELETE FROM ROUTE;
DELETE FROM BUS_STOP;

INSERT INTO BUS_STOP (stopID, stopName, street1, street2)
VALUES (222222, 'stop1', 'street1', NULL);

INSERT INTO ROUTE (routeID, S_firstStop, S_lastStop)
VALUES(159357, 222222, 222222);

INSERT INTO VISITS (R_routeID, S_stopID, arrivalTime, departTime)
VALUES(159357, 222222, '12:00:00', '12:00:30');
	-- bare minimum to have a visit record for a stop

DELETE FROM ROUTE
WHERE routeID = 159357;
	-- try removing a route
	-- CURRENT BEHAVIOR: fails by FK constraint to visits

SELECT routeID
FROM ROUTE;

SELECT R_routeID
FROM VISITS;
	-- shows a route and a visit record sharing a routeId

DELETE FROM VISITS
WHERE R_routeID = 159357;
	-- remove the visit record connected to the route

SELECT routeID
FROM ROUTE;

SELECT R_routeID
FROM VISITS;
	-- should show a route but no visit records

DELETE FROM VISITS;
DELETE FROM ROUTE;
DELETE FROM BUS_STOP;

-- visits R_route_name goes back to route route_name
DELETE FROM VISITS;
DELETE FROM ROUTE;
DELETE FROM BUS_STOP;

INSERT INTO BUS_STOP (stopID, stopName, street1, street2)
VALUES (222222, 'stop1', 'street1', NULL);

INSERT INTO ROUTE (routeID, S_firstStop, S_lastStop)
VALUES(111111, 222222, 222222);

INSERT INTO VISITS (R_routeID, S_stopID, arrivalTime, departTime)
VALUES(111111, 222222, '12:00:00', '12:00:30');
	-- route with a non-null name and a visit record

DELETE FROM VISITS;
DELETE FROM ROUTE;
DELETE FROM BUS_STOP;

-- visits S_stopId goes back to S_stopId
DELETE FROM VISITS;
DELETE FROM ROUTE;
DELETE FROM BUS_STOP;

INSERT INTO BUS_STOP (stopID, stopName, street1, street2)
VALUES (222222, 'stop1', 'street1', NULL);

INSERT INTO ROUTE (routeId, S_firstStop, S_lastStop)
VALUES(111111, 222222, 222222);

INSERT INTO VISITS (R_routeID, S_stopID, arrivalTime, departTime)
VALUES(111111, 222222, '12:00:00', '12:00:30');
	-- bus stop and a visit record

DELETE FROM BUS_STOP
WHERE stopID = 222222;
	-- try removing the bus stop
	-- CURRENT BEHAVIOR: fails by FK constraint to route,
	-- but not notified about visits

SELECT stopID
FROM BUS_STOP;

SELECT R_routeID
FROM VISITS;
	-- using R_routeId and not S_stopId because it's the primary key
	-- shows a bus stop and its visit record

DELETE FROM VISITS
WHERE S_stopID = 222222;
	-- remove the visit record

SELECT stopID
FROM BUS_STOP;

SELECT R_routeID
FROM VISITS;
	-- should show a bus stop without a visit record

DELETE FROM VISITS;
DELETE FROM ROUTE;
DELETE FROM BUS_STOP;

-- MITCH'S TESTS

-- route S_first_stop goes back to S_stopId
INSERT INTO BUS_STOP (stopID, stopName, street1, street2)
VALUES(780780, 'UW Bothell', '110 Ave NE', 'Campus Way NE');
INSERT INTO BUS_STOP (stopID, stopName, street1, street2)
VALUES(321321, 'Alderwood Mall', '184 St SW', 'Alderwood Mall Pkwy');
INSERT INTO ROUTE (routeID, S_firstStop, S_lastStop)
VALUES(159360, 780780, 321321);

-- route S_last_stop goes back to S_stopId
INSERT INTO ROUTE (routeID, S_firstStop, S_lastStop)
VALUES(159359, 321321, 780780);
-- scheduled R_route_id goes back to route routeId

INSERT INTO EMPLOYEE
VALUES (111222333, 'Jeff', 'L', 'Mason', '2018-09-30', NULL);
INSERT INTO BUS (busID, busName, capacity, manufactured_date, E_driver)
VALUES (22232, '535 Everett', 60, '2020-03-03', 111222333);

INSERT INTO SCHEDULED (R_routeID, B_busID, timeStart, timeEnd)
VALUES(159359, 22232, '12:54:00', '12:55:00');

-- scheduled B_busId goes back to bus busId
INSERT INTO ROUTE (routeID, S_firstStop, S_lastStop)
VALUES(357159, 321321, 780780);
INSERT INTO SCHEDULED (R_routeID, B_busID, timeStart, timeEnd)
VALUES(357159, 22232, '12:57:00', '12:59:00');
SELECT 
    *
FROM
    SCHEDULED
WHERE
    B_busID = 22222;