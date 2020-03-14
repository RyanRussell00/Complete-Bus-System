-- Tests all the foreign key constraints

-- PHIL'S TESTS

-- TEST: employee supervisor goes back to employee ssn
DELETE FROM EMPLOYEE;

INSERT INTO EMPLOYEE (ssn, Fname, Minit, Lname, street, city, state, zip, start_date, supervisor)
VALUES (111111111, 'Super', 'V', 'Isor', '123 1st Street', 'Redmond', 'WA', '98052', '2019-01-01', NULL);

INSERT INTO EMPLOYEE (ssn, Fname, Minit, Lname, street, city, state, zip, start_date, supervisor)
VALUES (222222222, 'Subo', 'R', 'Dinate', '456 2nd Street', 'Redmond', 'WA', '98052', '2020-02-01', 111111111);
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

INSERT INTO EMPLOYEE (ssn, Fname, Minit, Lname, street, city, state, zip, start_date, supervisor)
VALUES (111111111, 'Bus', 'D', 'River', '123 1st Street', 'Redmond', 'WA', '98052', '2020-01-01', NULL);

INSERT INTO BUS (busId, capacity, start_date, E_driver)
VALUES (11111, 20, NULL, 111111111);
	-- an employee and a bus, linked by an FK because the employee drives the bus

DELETE FROM EMPLOYEE
WHERE ssn = 111111111;
	-- try deleting the driver
	-- CURRENT BEHAVIOR: fails because employee has a foreign key in the bus

SELECT ssn
FROM EMPLOYEE;

SELECT busId, E_driver
FROM BUS;
	-- original bus and employee remain

UPDATE BUS
SET E_driver = NULL
WHERE busId = 11111;
	-- remove driver employee's key from the bus

DELETE FROM EMPLOYEE
WHERE ssn = 111111111;
	-- try deleting the driver again

SELECT ssn
FROM EMPLOYEE;

SELECT busId, E_driver
FROM BUS;
	-- no employees should remain
	-- bus should be driverless

DELETE FROM EMPLOYEE;
DELETE FROM BUS;

-- taps B_busId goes back to bus busId
DELETE FROM TAPS;
DELETE FROM CARD;
DELETE FROM FARE_TIER;
DELETE FROM BUS;

INSERT INTO BUS (busId, capacity, start_date, E_driver)
VALUES (11111, 20, NULL, NULL);

INSERT INTO FARE_TIER (tier, cost, fare_name)
VALUES (01, 2.50, NULL);

INSERT INTO CARD (card_number, balance, expiry_date, F_fare)
VALUES (111111111, 25.00, '2020-12-01', 01);

INSERT INTO TAPS (B_busId, C_card_num, time_stamp)
VALUES (11111, 111111111, '2020-03-01 10:00:00');
	-- bare minimum records for a taps and bus relationship

DELETE FROM BUS
WHERE busId = 11111;
	-- try deleting the bus
	-- CURRENT BEHAVIOR: fails by FK constraint to taps

SELECT busId
FROM BUS;

SELECT B_busId, C_card_num, time_stamp
FROM TAPS;
	-- shows a bus and a tap record

DELETE FROM TAPS
WHERE B_busId = 11111;
	-- remove tap records

SELECT busId
FROM BUS;

SELECT B_busId, C_card_num, time_stamp
FROM TAPS;
	-- should show a bus and no tap record
	
DELETE FROM TAPS;
DELETE FROM BUS;

-- taps C_card_num goes back to card cardNum
DELETE FROM TAPS;
DELETE FROM BUS;
DELETE FROM CARD;
DELETE FROM FARE_TIER;

INSERT INTO FARE_TIER (tier, cost, fare_name)
VALUES (01, 2.50, NULL);

INSERT INTO CARD (card_number, balance, expiry_date, F_fare)
VALUES (111111111, 25.00, '2020-12-01', 01);

INSERT INTO BUS (busId, capacity, start_date, E_driver)
VALUES (11111, 20, NULL, NULL);

INSERT INTO TAPS (B_busId, C_card_num, time_stamp)
VALUES (11111, 111111111, '2020-03-01 10:00:00');
	-- bare minimum for a taps and card relationship

DELETE FROM CARD
WHERE card_number = 111111111;
	-- try deleting a card
	-- CURRENT BEHAVIOR: fails by FK constraint to taps

SELECT card_number
FROM CARD;

SELECT B_busId, C_card_num, time_stamp
FROM TAPS;
	-- shows a card and a tap record

DELETE FROM TAPS
WHERE C_card_num = 111111111;
	-- remove tap record

SELECT card_number
FROM CARD;

SELECT B_busId, C_card_num, time_stamp
FROM TAPS;
	-- should show a card but no tap records

DELETE FROM TAPS;
DELETE FROM CARD;

-- card F_fare goes back to faretier tier
DELETE FROM CARD;
DELETE FROM FARE_TIER;

INSERT INTO FARE_TIER (tier, cost, fare_name)
VALUES (01, 2.50, NULL);

INSERT INTO CARD (card_number, balance, expiry_date, F_fare)
VALUES (111111111, 25.00, '2020-12-01', 01);
	-- create a card connected to a fare tier

DELETE FROM FARE_TIER
WHERE tier = 01;
	-- try removing the fare tier
	-- CURRENT BEHAVIOR: fails because of an FK constraint to card

SELECT tier
FROM FARE_TIER;

SELECT card_number
FROM CARD;
	-- shows a fare tier and a card with that tier

DELETE FROM CARD
WHERE card_number = 111111111;
	-- remove the card

SELECT tier
FROM FARE_TIER;

SELECT card_number
FROM CARD;
	-- should show a fare tier but not card

DELETE FROM CARD;
DELETE FROM FARE_TIER;

-- visits R_routeId goes back to route routeId
DELETE FROM VISITS;
DELETE FROM ROUTE;
DELETE FROM BUS_STOP;

INSERT INTO BUS_STOP (stopId, stop_name, street1, street2)
VALUES (222222, 'stop1', 'street1', NULL);

INSERT INTO ROUTE (routeId, route_name, S_first_stopId, S_last_stopId)
VALUES(111111, NULL, 222222, 222222);

INSERT INTO VISITS (R_routeId, R_route_name, S_stopId, arrival_time, depart_time)
VALUES(111111, NULL, 222222, '12:00:00', '12:00:30');
	-- bare minimum to have a visit record for a stop

DELETE FROM ROUTE
WHERE routeId = 111111;
	-- try removing a route
	-- CURRENT BEHAVIOR: fails by FK constraint to visits

SELECT routeId
FROM ROUTE;

SELECT R_routeId
FROM VISITS;
	-- shows a route and a visit record sharing a routeId

DELETE FROM VISITS
WHERE R_routeId = 111111;
	-- remove the visit record connected to the route

SELECT routeId
FROM ROUTE;

SELECT R_routeId
FROM VISITS;
	-- should show a route but no visit records

DELETE FROM VISITS;
DELETE FROM ROUTE;
DELETE FROM BUS_STOP;

-- visits R_route_name goes back to route route_name
DELETE FROM VISITS;
DELETE FROM ROUTE;
DELETE FROM BUS_STOP;

INSERT INTO BUS_STOP (stopId, stop_name, street1, street2)
VALUES (222222, 'stop1', 'street1', NULL);

INSERT INTO ROUTE (routeId, route_name, S_first_stopId, S_last_stopId)
VALUES(111111, 'route1', 222222, 222222);

INSERT INTO VISITS (R_routeId, R_route_name, S_stopId, arrival_time, depart_time)
VALUES(111111, 'route1', 222222, '12:00:00', '12:00:30');
	-- route with a non-null name and a visit record

DELETE FROM ROUTE
WHERE route_name = 'route1';
	-- try removing a route using its name
	-- CURRENT BEHAVIOR: fails by FK constraint to visits

SELECT route_Name
FROM ROUTE;

SELECT R_route_name
FROM VISITS;
	-- shows a route and a visit record sharing a routeId

DELETE FROM VISITS
WHERE R_route_name = 'route1';
	-- remove the visit record connected to the route

SELECT route_Name
FROM ROUTE;

SELECT R_route_name
FROM VISITS;
	-- should show a route but no visit records

DELETE FROM VISITS;
DELETE FROM ROUTE;
DELETE FROM BUS_STOP;

-- visits S_stopId goes back to S_stopId
DELETE FROM VISITS;
DELETE FROM ROUTE;
DELETE FROM BUS_STOP;

INSERT INTO BUS_STOP (stopId, stop_name, street1, street2)
VALUES (222222, 'stop1', 'street1', NULL);

INSERT INTO ROUTE (routeId, route_name, S_first_stopId, S_last_stopId)
VALUES(111111, NULL, 222222, 222222);

INSERT INTO VISITS (R_routeId, R_route_name, S_stopId, arrival_time, depart_time)
VALUES(111111, NULL, 222222, '12:00:00', '12:00:30');
	-- bus stop and a visit record

DELETE FROM BUS_STOP
WHERE stopId = 222222;
	-- try removing the bus stop
	-- CURRENT BEHAVIOR: fails by FK constraint to route,
	-- but not notified about visits

SELECT stopId
FROM BUS_STOP;

SELECT R_routeId
FROM VISITS;
	-- using R_routeId and not S_stopId because it's the primary key
	-- shows a bus stop and its visit record

DELETE FROM VISITS
WHERE S_stopId = 222222;
	-- remove the visit record

SELECT stopId
FROM BUS_STOP;

SELECT R_routeId
FROM VISITS;
	-- should show a bus stop without a visit record

DELETE FROM VISITS;
DELETE FROM ROUTE;
DELETE FROM BUS_STOP;

-- MITCH'S TESTS

-- route S_first_stop goes back to S_stopId
INSERT INTO BUS_STOP
VALUES(780780, 'UW Bothell', '110 Ave NE', 'Campus Way NE');
INSERT INTO ROUTE
VALUES(159360, 'Lynnwood', 780780, 321321);

-- route S_last_stop goes back to S_stopId
INSERT INTO ROUTE
VALUES(159359, 'Bellevue', 123132, 780780);
-- scheduled R_route_id goes back to route routeId

INSERT INTO BUS
VALUES (22232, 60, '2020-03-03', 111222333);

INSERT INTO SCHEDULED
VALUES(159360, 'Lynnwood', 22232, '12:54:00', '12:55:00');


-- scheduled R_route_name goes back to route route_name
INSERT INTO SCHEDULED
VALUES(357159, 'Everett', 22232, '12:54:00', '12:55:00');

SELECT 
    *
FROM
    SCHEDULED
WHERE
    R_route_name = 'Lynnwood'
        AND time_start >= '13:30:00';


-- scheduled B_busId goes back to bus busId
INSERT INTO SCHEDULED
VALUES(357159, 'Everett', 22232, '12:57:00', '12:59:00');
SELECT 
    *
FROM
    SCHEDULED
WHERE
    B_busId = 22222;