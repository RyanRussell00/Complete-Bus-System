DELETE FROM VISITS;
DELETE FROM ROUTE;
DELETE FROM BUS_STOP;
DELETE FROM BUS;

INSERT INTO BUS
	(busID, capacity, manufactured_date, E_driver)
VALUES
	(11111, 20, '2000-01-01', NULL),
	(22222, 20, '2000-01-01', NULL),
	(33333, 20, '2000-01-01', NULL),
	(44444, 20, '2000-01-01', NULL);

INSERT INTO BUS_STOP
	(stopId, street1, street2)
VALUES
	(000001, '1st Street', NULL),
	(000002, '2nd Street', NULL),
	(000003, '3rd Street', NULL),
	(000004, '4th Street', NULL),
	(000005, '5th Street', NULL),
	(000006, '6th Street', NULL),
	(000007, '7th Street', NULL),
	(000008, '8th Street', NULL);

INSERT INTO ROUTE
	(routeID, routeName, S_firstStop, S_lastStop)
VALUES
	(001, 'Redmond', 000001, 000006),
	(002, 'Bellevue', 000007, 000008);

INSERT INTO VISITS
	(R_routeID, R_routeName, S_stopID, typeOfDay, arrivalTime, departTime)
VALUES
	(001, 'Redmond', 000001, 'Weekday', '12:00:00', '12:05:00'),
	(001, 'Redmond', 000002, 'Weekday', '12:06:00', '12:09:00'),
	(001, 'Redmond', 000003, 'Weekday', '12:10:00', '12:15:00'),
	(001, 'Redmond', 000004, 'Weekday', '12:16:00', '12:19:00'),
	(001, 'Redmond', 000005, 'Weekend', '12:00:00', '12:05:00'),
	(001, 'Redmond', 000006, 'Weekend', '12:06:00', '12:10:00'),
	(002, 'Bellevue', 000007, 'Weekday', '12:00:00', '12:05:00'),
	(002, 'Bellevue', 000008, 'Weekday', '12:06:00', '12:10:00');

INSERT INTO SCHEDULED
	(R_routeID, R_routeName, B_busID, timeStart, timeEnd)
VALUES
	(001, 'Redmond', 11111, '2020-03-10 08:00:00', '2020-03-10 11:00:00'),
	(001, 'Redmond', 22222, '2020-03-10 11:30:00', '2020-03-10 16:00:00'),
	(002, 'Bellevue', 33333, '2020-03-10 08:00:00', '2020-03-10 11:00:00'),
	(002, 'Bellevue', 44444, '2020-03-10 11:30:00', '2020-03-10 16:00:00');

SELECT
	b.busID,
	TIMESTAMP(DATE(sc.timeStart), v.arrivalTime),
	TIMESTAMP(DATE(sc.timeStart), v.departTime)
FROM BUS b, VISITS v, SCHEDULED sc
WHERE v.typeOfDay = 'Weekday'
	AND sc.B_busID = b.busID
	AND sc.R_routeID = v.R_routeID
	AND sc.R_routeName = v.R_routeName
	AND TIME(sc.timeStart) <= v.arrivalTime
	AND TIME(sc.timeEnd) >= v.departTime
ORDER BY b.busID ASC, TIMESTAMP(sc.timeStart, v.arrivalTime) ASC;

DELETE FROM VISITS;
DELETE FROM ROUTE;
DELETE FROM BUS_STOP;
DELETE FROM BUS;