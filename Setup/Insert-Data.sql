USE CBS; 

-- Delete all data from EMPLOYEE before inserting
-- DELETE FROM EMPLOYEE;

INSERT INTO EMPLOYEE (ssn, Fname, Minit, Lname, startDate, supervisor)
VALUES (123456789, 'Mason', 'G', 'Kim','2019-09-05', NULL);

INSERT INTO EMPLOYEE (ssn, Fname, Minit, Lname, startDate, supervisor)
VALUES (112233445, 'Jason', 'F', 'Dry', '2019-12-20', 123456789);

INSERT INTO EMPLOYEE
VALUES (111222333, 'Jeff', 'L', 'Mason', '2018-09-30', 123456789);

INSERT INTO ADDRESS (S_ssn, street, city, state, zip) 
VALUES (123456789, 'Campus', 'Seattle', 'WA', '98195');

INSERT INTO ADDRESS (S_ssn, street, city, state, zip) 
VALUES (112233445, '18115 Campus Way NE', 'Bothell', 'WA', '98011');

INSERT INTO ADDRESS (S_ssn, street, city, state, zip) 
VALUES (111222333, 'Make This St', 'Lynnwood', 'WA', '98087');
-- Delete all data from BUS before inserting
-- DELETE FROM BUS;

INSERT INTO BUS (busID, busName, capacity, manufactured_date, E_driver)
VALUES (11111, '535 Lynnwood', 60, '2020-01-01', 111222333);

INSERT INTO BUS (busID, busName, capacity, manufactured_date, E_driver)
VALUES (22222, '535 Bellevue', 60, '2020-01-01', 112233445);

-- Delete all data from FARE_TIER before inserting
-- DELETE FROM FARE_TIER;

INSERT INTO FARE_TIER (tier, cost, fareName)
VALUES (1, 1, 'Veteran');

INSERT INTO FARE_TIER (tier, cost, fareName)
VALUES (2, 1, 'Disabled');

INSERT INTO FARE_TIER (tier, cost, fareName)
VALUES (3, 1.5, 'Student');

INSERT INTO FARE_TIER (tier, cost, fareName)
VALUES (4, 1.5, 'Child');

INSERT INTO FARE_TIER (tier, cost, fareName)
VALUES (5, 2.75, 'Adult');

INSERT INTO FARE_TIER (tier, cost, fareName)
VALUES (6, 1, 'Senior');

-- Delete all data from CARD before inserting
-- DELETE FROM CARD;

INSERT INTO CARD (cardNum, balance, expiry_date, F_fare)
VALUES(456789123, 99.99, '2022-09-20', 3); -- Some student

INSERT INTO CARD (cardNum, balance, expiry_date, F_fare)
VALUES(789456123, 99.99, '2022-10-20', 3); -- Some student

INSERT INTO CARD (cardNum, balance, expiry_date, F_fare)
VALUES(987654321, 4.69, '2022-09-20', 1); -- Some Veteran

INSERT INTO CARD (cardNum, balance, expiry_date, F_fare)
VALUES(321654987, 23.69, '2022-10-20', 4); -- Some Child

-- Delete all data from TAPS before inserting
-- DELETE FROM TAPS;

INSERT INTO TAPS (B_busID, C_cardNum, time_stamp)
VALUES(11111, 321654987, '2020-06-20 15:20:39');

INSERT INTO TAPS (B_busID, C_cardNum, time_stamp)
VALUES(11111, 987654321, '2019-12-07 20:20:20');

INSERT INTO TAPS (B_busID, C_cardNum, time_stamp)
VALUES(22222, 987654321, '2020-11-14 07:21:49');

-- Delete all data from BUS_STOP before inserting
-- DELETE FROM BUS_STOP;

INSERT INTO BUS_STOP (stopID, stopName, street1, street2)
VALUES(123132, 'UW Bothell', '110 Ave NE', 'Campus Way NE');

INSERT INTO BUS_STOP (stopID, stopName, street1, street2)
VALUES(321321, 'Lynnwood Transit', '200th ST SW', '46th Ave W');

INSERT INTO BUS_STOP (stopID, stopName, street1, street2)
VALUES(654789, 'South Everett', '112th St SE', 'South Everett St');

-- Delete all data from ROUTE before inserting
-- DELETE FROM ROUTE;

INSERT INTO ROUTE (routeID, S_firstStop, S_lastStop)
VALUES(159357, 123132, 321321);

INSERT INTO ROUTE (routeID, S_firstStop, S_lastStop)
VALUES(357159, 321321, 654789);

INSERT INTO ROUTE (routeID, S_firstStop, S_lastStop)
VALUES(965874, 654789, 123132);

-- Delete all data from VISITS before inserting
-- DELETE FROM VISITS;

INSERT INTO VISITS (R_routeID, S_stopID, arrivalTime, departTime)
VALUES(159357, 123132, '16:30:10', '16:30:40');

INSERT INTO VISITS (R_routeID, S_stopID, arrivalTime, departTime)
VALUES(357159, 321321, '06:29:11', '06:29:38');

INSERT INTO VISITS (R_routeID, S_stopID, arrivalTime, departTime)
VALUES(965874, 654789, '21:01:57', '21:01:57');

-- Delete all data from SCHEDULED before inserting
-- DELETE FROM SCHEDULED;

INSERT INTO SCHEDULED (R_routeID, B_busID, timeStart, timeEnd)
VALUES(159357, 11111, '15:01:57', '21:01:57');

INSERT INTO SCHEDULED (R_routeID, B_busID, timeStart, timeEnd)
VALUES(159357, 22222, '19:20:33', '20:08:57');