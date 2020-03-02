-- TEST: employee supervisor goes back to employee ssn
DELETE FROM EMPLOYEE;

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

-- taps C_card_num goes back to card cardNum

-- card F_fare goes back to faretier tier

-- visits R_routeId goes back to route routeId

-- visits R_route_name goes back to route route_name

-- visits S_stopId goes back to S_stopId

-- route S_first_stop goes back to S_stopId

-- route S_last_stop goes back to S_stopId

-- scheduled R_route_id goes back to route routeId

-- scheduled R_route_name goes back to route route_name

-- B_busId goes back to bus busId

