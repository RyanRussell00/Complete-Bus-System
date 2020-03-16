-- TEST: employee supervisor goes back to employee ssn
DELETE FROM EMPLOYEE;

INSERT INTO EMPLOYEE (ssn, Fname, Minit, Lname, startDate, supervisor)
VALUES (111111111, 'Super', 'V', 'Isor', '2019-01-01', NULL);
INSERT INTO ADDRESS (E_ssn, street, city, state, zip) 
VALUES (111111111, '123 1st Street', 'Redmond', 'WA', '98052');

INSERT INTO EMPLOYEE (ssn, Fname, Minit, Lname, startDate, supervisor)
VALUES (222222222, 'Subo', 'R', 'Dinate', '2020-02-01', 111111111);
INSERT INTO ADDRESS (E_ssn, street, city, state, zip) 
VALUES (222222222, '456 2nd Street', 'Redmond', 'WA', '98052');
	-- a manager and their subordinate, linked by an FK

SELECT ssn, supervisor
FROM EMPLOYEE;
	-- should show two employees, one managing the other

DELETE FROM EMPLOYEE
WHERE ssn = 111111111;
	-- removing the supervisor should not affect the subordinate employee
	
SELECT ssn, supervisor
FROM EMPLOYEE;
	-- should show only the remaining subordinate
	-- WORKS!
	
DELETE FROM EMPLOYEE;