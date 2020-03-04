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

DELETE FROM TAPS
WHERE B_busId = 11111;
	-- remove taps records

DELETE FROM BUS
WHERE busId = 11111;
	-- removes the bus this time

SELECT busId
FROM BUS;

SELECT B_busId, C_card_num, time_stamp
FROM TAPS;
	-- should be no more bus and taps records
	
DELETE FROM BUS;
DELETE FROM TAPS;

-- taps C_card_num goes back to card cardNum

-- card F_fare goes back to faretier tier

-- visits R_routeId goes back to route routeId

-- visits R_route_name goes back to route route_name

-- visits S_stopId goes back to S_stopId

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
