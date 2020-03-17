-- Testing on delete and on cascade of employee
--    deleting supervisor ssn should set the supervisor ssn to null for all employees with that supervisor

-- SELECT * FROM EMPLOYEE;
-- DELETE FROM EMPLOYEE
-- WHERE ssn = 123456789;
-- SELECT * FROM EMPLOYEE;

-- THIS ONE DOES NOT WORK!! SELF_REFERENCING    
-- updating supervisor ssn should cascade that ssn to all employees that have that supervisor
-- SELECT * FROM EMPLOYEE;
-- UPDATE EMPLOYEE
-- SET ssn = 999999999
-- WHERE ssn = 123456789;
-- SELECT * FROM EMPLOYEE;


-- Testing ON DELETE CASCADE of address E_ssn
-- If E_ssn of address is removed, then remove the addresss
SELECT * FROM EMPLOYEE;
SELECT * FROM ADDRESS;
DELETE FROM EMPLOYEE
WHERE ssn = 123456789;
SELECT * FROM EMPLOYEE;
SELECT * FROM ADDRESS;

-- Testing ON UPDATE CASCADE
-- If E_ssn of address is changed, then change the ssn address
SELECT * FROM EMPLOYEE;
SELECT * FROM ADDRESS;
UPDATE EMPLOYEE
SET ssn = 999999999
WHERE ssn = 112233445;
SELECT * FROM EMPLOYEE;
SELECT * FROM ADDRESS;

-- Testing on delete and on cascade of address bus
-- If E_driver is removed, then set the bus employee to null

-- SELECT * FROM EMPLOYEE;
-- SELECT * FROM BUS;
-- DELETE FROM EMPLOYEE
-- WHERE ssn = 112233445;
-- SELECT * FROM EMPLOYEE;
-- SELECT * FROM BUS;

-- If E_driver is updated, then set the bus employee to that employee ssn

-- SELECT * FROM EMPLOYEE;
-- SELECT * FROM BUS;
-- UPDATE EMPLOYEE
-- SET ssn = 999999999
-- WHERE ssn = 112233445;
-- SELECT * FROM EMPLOYEE;
-- SELECT * FROM BUS;


-- Testing on delete and on cascade of address bus
-- Since "Taps must have busId and card_number" then a taps tuple will be deleted if either a bus id or card_number is deleted

-- SELECT * FROM BUS;
-- SELECT * FROM TAPS;
-- DELETE FROM BUS
-- WHERE busID = 11111;
-- SELECT * FROM BUS;
-- SELECT * FROM TAPS;

-- SELECT * FROM CARD;
-- SELECT * FROM TAPS;
-- DELETE FROM CARD
-- WHERE cardNum = 987654321;
-- SELECT * FROM CARD;
-- SELECT * FROM TAPS;

-- If card/bus id is changed, then taps should reflect those changes

-- SELECT * FROM BUS;
-- SELECT * FROM TAPS;
-- UPDATE BUS
-- SET busID = 33333
-- WHERE busID = 11111;
-- SELECT * FROM BUS;
-- SELECT * FROM TAPS;

-- SELECT * FROM CARD;
-- SELECT * FROM TAPS;
-- UPDATE CARD
-- SET cardNum = 555555555
-- WHERE cardNum = 987654321;
-- SELECT * FROM CARD;
-- SELECT * FROM TAPS;
