INSERT INTO BUS_STOP
	(stopId, street1, street2)
VALUES
	(000001, '1st Street', NULL);
	(000002, '2nd Street', NULL);
	(000003, '3rd Street', NULL);
	(000004, '4th Street', NULL);
	(000005, '5th Street', NULL);
	(000006, '6th Street', NULL);
	(000007, '7th Street', NULL);
	(000008, '8th Street', NULL);

INSERT INTO ROUTE
	(routeID, routeName, S_firstStop, S_lastStop)
VALUES
	(001, '100 Redmond', 000001, 000006);
	(002, '200 Bellevue', 000007, 000008);

INSERT INTO VISITS
	(R_routeId, S_stopID, typeOfDay, arrivalTime, departTime)
VALUES
	(001, 000001, 'Weekday', 12:00:00, 12:00:01);

SELECT v.arrivalTime, v.S_stopID
FROM VISITS v, ROUTE r
where v.R_routeID = r.routeID
	AND r.routeName = '535 Lynnwood'
	AND v.typeOfDay = 'Weekday'
ORDER BY v.arrivalTime ASC;