DELETE FROM VISITS;
DELETE FROM ROUTE;
DELETE FROM BUS_STOP;

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

SELECT v.arrivalTime, v.S_stopID
FROM VISITS v, ROUTE r
WHERE v.R_routeID = r.routeID
	AND r.routeID = 001
	AND r.routeName = 'Redmond'
	AND v.typeOfDay = 'Weekday'
ORDER BY v.arrivalTime ASC;

DELETE FROM VISITS;
DELETE FROM ROUTE;
DELETE FROM BUS_STOP;