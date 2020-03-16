DELETE FROM SCHEDULED;
DELETE FROM ROUTE;
DELETE FROM BUS_STOP;
DELETE FROM TAPS;
DELETE FROM BUS;
DELETE FROM CARD;

INSERT INTO CARD
	(cardNum, balance, expiry_date, F_fare)
VALUES
	(111111111, 50.00, '2021-12-31', 5),
	(222222222, 25.00, '2022-01-01', 4);

INSERT INTO BUS
	(busID, capacity, manufactured_date, E_driver)
VALUES
	(11111, 20, '2000-01-01', NULL),
	(22222, 20, '2000-01-01', NULL),
	(33333, 20, '2000-01-01', NULL),
	(44444, 20, '2000-01-01', NULL);

INSERT INTO TAPS
	(B_busID, C_cardNum, time_stamp)
VALUES
	(11111, 111111111, '2020-03-10 12:00:00'),
	(22222, 111111111, '2020-03-10 12:05:00'),
	(33333, 111111111, '2020-03-09 12:00:00'),
	(44444, 111111111, '2020-03-09 12:05:00'),
	(11111, 222222222, '2020-03-10 12:00:00'),
	(22222, 222222222, '2020-03-10 12:00:00');

INSERT INTO BUS_STOP
	(stopId, street1, street2)
VALUES
	(100001, '1st Street', NULL),
	(100002, '2nd Street', NULL),
	(100003, '3rd Street', NULL),
	(100004, '4th Street', NULL),
	(100005, '5th Street', NULL),
	(100006, '6th Street', NULL),
	(100007, '7th Street', NULL),
	(100008, '8th Street', NULL);

INSERT INTO ROUTE
	(routeID, routeName, S_firstStop, S_lastStop)
VALUES
	(100, 'Redmond', 100001, 100002),
	(100, 'Seattle', 100002, 100003),
	(200, 'Redmond', 100003, 100004),
	(200, 'Seattle', 100004, 100005),
	(300, 'Bellevue', 100005, 100006),
	(300, 'Kirkland', 100006, 100007),
	(400, 'Woodinville', 100007, 100008);

INSERT INTO SCHEDULED
	(R_routeID, R_routeName, B_busID, timeStart, timeEnd)
VALUES
	(100, 'Redmond', 11111, '2020-03-10 9:00:00', '2020-03-10 15:00:00'),
	(100, 'Redmond', 44444, '2020-03-09 08:30:00', '2020-03-09 1:00:00'),
	(100, 'Seattle', 11111, '2020-03-10 15:30:00', '2020-03-10 17:00:00'),
	(200, 'Redmond', 22222, '2020-03-10 09:00:00', '2020-03-10 13:00:00'),
	(200, 'Seattle', 33333, '2020-03-09 11:00:00', '2020-03-09 15:00:00'),
	(300, 'Bellevue', 11111, '2020-03-10 09:00:00', '2020-03-10 15:00:00'),
	(300, 'Kirkland', 44444, '2020-03-08 01:00:00', '2020-03-12 23:00:00');

SELECT sc.R_routeID, sc.R_routeName, t.time_stamp, f.cost
FROM FARE_TIER f, CARD c, TAPS t, SCHEDULED sc
WHERE c.cardNum = 111111111
	AND t.C_cardNum = c.cardNum
	AND c.F_fare = f.tier
	AND t.B_busID = sc.B_busID
	AND t.time_stamp >= sc.timeStart
	AND t.time_stamp <= sc.timeEnd
ORDER BY t.time_stamp ASC;

DELETE FROM SCHEDULED;
DELETE FROM ROUTE;
DELETE FROM BUS_STOP;
DELETE FROM TAPS;
DELETE FROM BUS;
DELETE FROM CARD;