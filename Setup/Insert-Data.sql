USE CBS; 

-- Delete all data from EMPLOYEE before inserting
DELETE FROM EMPLOYEE;

INSERT INTO EMPLOYEE
VALUES (123456789, 'Mason', 'G', 'Kim', 'Campus', 'Seattle', 'WA', '98195',  '2019-09-05', 111111111);

INSERT INTO EMPLOYEE
VALUES (112233445, 'Jason', 'F', 'Dry', '18115 Campus Way NE', 'Bothell', 'WA', '98011',  '2019-12-20', 123456789);

INSERT INTO EMPLOYEE
VALUES (111222333, 'Jeff', 'L', 'Mason', 'Make This St', 'Lynnwood', 'WA', '98087',  '2018-09-30', 123456789);

-- Delete all data from BUS before inserting
DELETE FROM BUS;

INSERT INTO BUS
VALUES (11111, 60, '2020-01-01', 111222333);

INSERT INTO BUS
VALUES (22222, 60, '2020-01-01', 112233445);

-- Delete all data from FARE_TIER before inserting
DELETE FROM FARE_TIER;

INSERT INTO FARE_TIER
VALUES (1, 1, 'Veteran');

INSERT INTO FARE_TIER
VALUES (2, 1, 'Disabled');

INSERT INTO FARE_TIER
VALUES (3, 1.5, 'Student');

INSERT INTO FARE_TIER
VALUES (4, 1.5, 'Child');

INSERT INTO FARE_TIER
VALUES (5, 2.75, 'Adult');

INSERT INTO FARE_TIER
VALUES (6, 1, 'Senior');

-- Delete all data from CARD before inserting
DELETE FROM CARD;

INSERT INTO CARD
VALUES(456789123, 99.99, '2022-09-20', 3); -- Some student

INSERT INTO CARD
VALUES(789456123, 99.99, '2022-10-20', 3); -- Some student

INSERT INTO CARD
VALUES(987654321, 4.69, '2022-09-20', 1); -- Some Veteran

INSERT INTO CARD
VALUES(321654987, 23.69, '2022-10-20', 4); -- Some Child

-- Delete all data from TAPS before inserting
DELETE FROM TAPS;

INSERT INTO TAPS
VALUES(11111, 321654987, '2020-06-20 15:20:39');

INSERT INTO TAPS
VALUES(11111, 987654321, '2019-12-07 20:20:20');

INSERT INTO TAPS
VALUES(22222, 987654321, '2020-11-14 07:21:49');

-- Delete all data from BUS_STOP before inserting
DELETE FROM BUS_STOP;

INSERT INTO BUS_STOP
VALUES(123132, 'UW Bothell', '110 Ave NE', 'Campus Way NE');

INSERT INTO BUS_STOP
VALUES(321321, 'Lynnwood Transit Center', '200th ST SW', '46th Ave W');

INSERT INTO BUS_STOP
VALUES(654789, 'South Everett Freeway Station', '112th St SE', 'South Everett St');

-- Delete all data from ROUTE before inserting
DELETE FROM ROUTE;

INSERT INTO ROUTE
VALUES(159357, 'Bothell to Lynnwood', 123132, 321321);

INSERT INTO ROUTE
VALUES(357159, 'Lynnwood to Everett', 321321, 654789);

INSERT INTO ROUTE
VALUES(965874, 'Bothell to Everett', 123132, 654789);

-- Delete all data from VISITS before inserting
DELETE FROM VISITS;

-- INSERT INTO VISITS
-- VALUES(123132, 'Bothell to Lynnwood', 'stopid1', '16:30:10', '16:30:40');

-- INSERT INTO VISITS
-- VALUES(321321, 'Bothell to Lynnwood', 'stopid1', '16:30:10', '16:30:40');

-- INSERT INTO VISITS
-- VALUES(654789, 'Bothell to Lynnwood', 'stopid1', '16:30:10', '16:30:40');