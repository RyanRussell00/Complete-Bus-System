from datetime import datetime, timedelta, date

from Database import *;
from CommonFunctions import *;

# Ending semicolons intentionally left out because the sanitize function removes all semicolons
SELECT_QUERY = "SELECT %s FROM %s WHERE %s"
SELECT_ALL_QUERY = "SELECT %s FROM %s"
NEW_EMPLOYEE_INSERT = "INSERT INTO EMPLOYEE (ssn, Fname, Minit, Lname, startDate, supervisor) VALUES (%s)"
SELECT_EMPL_ROUTE_QUERY = "SELECT %s FROM %s WHERE %s IN (SELECT %s FROM %s WHERE %s)"
SELECT_EMPL_SCHEDULE = "SELECT %s FROM %s WHERE % (SELECT %s FROM %s WHERE %s)"
ADDRESS_INSERT_UPDATE = "INSERT INTO ADDRESS (E_ssn, street, city, state, zip) VALUES (%s, '%s', '%s', '%s', '%s') " \
                        "ON DUPLICATE KEY UPDATE street = '%s', city = '%s', state = '%s', zip = '%s';"
EMPLOYEE_INFORMATION_QUERY = "SELECT * FROM EMPLOYEE AS E LEFT JOIN ADDRESS AS A ON E.ssn = A.E_ssn WHERE E.ssn = %s";
# Semicolon left out intentionally
# I have an employee on a bus and they want to know what their stop order is
VISIT_QUERY = "SELECT v.arrivalTime, v.S_stopID FROM VISITS v, ROUTE r WHERE v.R_routeID = r.routeID AND r.routeID = %s" \
              " AND r.routeName = '%s' AND v.typeOfDay = '%s' ORDER BY v.arrivalTime ASC";


# Gets all stops on a bus's route on a given type of date
# Use Case: I want to know at what time the 535 Lynnwood will be at each of its stops on March 15 2020
def CheckSchedule():
    SeparatingLine();

    # Dictionary (map) to receive multiple inputs from user
    reqDict = {"Route Number (3 digits)": "",
               "Route Name": "",
               "Day": ""
               };
    reqDict["Day"] = GetDay();
    for key in reqDict:
        while (reqDict[key] == ""):
            print("Please enter the " + key + " \n" +
                  "Or enter 'X' at any time to exit the program.");
            entry = input(key + ": ");
            entry = entry.strip();
            if (entry.upper() == "X"):
                EndProgram();
            # Ensure Route number is valid
            if (key == "Route Number (3 digits)"):
                if (len(entry) == 3):
                    try:
                        int(entry);
                    except ValueError:
                        entry = "";
                        print("Invalid Input: Route Number must be exactly 3 numbers long.");
                else:
                    entry = "";
            elif (key == "Route Name"):
                if (len(entry) == 0 or len(entry) > 20):
                    entry = "";
            reqDict[key] = entry;

    allValues = [];
    for val in reqDict.values():
        allValues.append(val);
    print(allValues);
    if (len(allValues) != 3):
        print("Something went wrong with inputting data.");
        return False;
    query = VISIT_QUERY % (allValues[0], allValues[1], allValues[2]);
    print(query);

    result = SubmitQuery(query);
    # global variable accessible anywhere to get Employee's name
    if (result is False):
        print("Error Submitting Query.");
        return False;
    # If the result is empty that means the system returned an empty set
    elif (len(result) == 0):
        print("Empty Set: No values exist for request.")
        return False;
    else:
        print("Arrival Time  |  Stop ID");
        for line in result:
            print(DisplayClean(line));
    return True;


# Validates an employee is valid
def ValidateEmployee():
    ssn = "";
    valid = False;
    while (not valid):
        print("Please enter the Social Security Number (9 digits) of the Employee you want to access. \n"
              "Or enter X to exit the program.");
        ssn = input("Enter SSN: ");

        if (ssn.upper() == "X"):
            EndProgram();
            break;
        elif (len(ssn) != 9):
            print("SSN must be 9 digits long.");
            continue;

        try:
            int(ssn);
            valid = True;
        except ValueError:
            print("SSN must be a number.");
            continue;

    query = (SELECT_QUERY % ("Fname, Lname", "EMPLOYEE", "ssn = " + ssn));
    result = SubmitQuery(query);
    # global variable accessible anywhere to get Employee's name
    if (result is None or len(result) != 1):
        print("Could not locate employee with given SSN");
        return None;
    else:
        name = ""
        for n in result:
            name += n;
    emp = (ssn, name)
    return emp;


# Sets the current employee
def SetCurrentEmployee():
    SeparatingLine();
    emp = ValidateEmployee();
    if (emp is None or len(emp) < 2):
        return False;

    global ssn;
    ssn = DisplayClean(emp[0]);
    global name;
    name = DisplayClean(emp[1]);
    if (ssn == "" or name == ""):
        print("Error: SSN or Name is empty.")
        return False;
    return True;


# Options for the employee
def EmployeeQueries():
    if (not SetCurrentEmployee()):
        print("Error trying to get employee. Please contact your system administrator.");

    SeparatingLine();
    choice = "";
    while (choice == ""):
        print("Get Employee's information: I \n"
              "Get the buses that the Employee is assigned to: B \n"
              "Get the routes and times that the Employee is driving: R \n"
              "End program: X");
        choice = input("Please enter a command: ").upper();

    query = "";
    if (choice == "I"):
        # Join the employee table and the address table to get the full employee's information
        # print(ssn + "\n");

        # query = (SELECT_QUERY % ("*", "EMPLOYEE AS E LEFT JOIN ADDRESS AS A ON E.ssn = A.E_ssn", "E_ssn = " + ssn));
        query = EMPLOYEE_INFORMATION_QUERY % ssn;

        # query = SELECT_ALL_QUERY % ("*", "EMPLOYEE");
        # employeeAddressQuery = "SELECT * FROM EMPLOYEE AS E, ADDRESS AS A WHERE E.ssn = " + ssn + " AND A.E_ssn = " + ssn;
        # addressQuery = SELECT_QUERY % ("*", "ADDRESS", "E_ssn = " + ssn);

    elif (choice == "B"):
        # Gets all busses that the employee is assigned to
        query = SELECT_QUERY % ("busID", "BUS", "E_driver = " + ssn);
    elif (choice == "R"):
        # Gets all routes that the employee is assigned to
        query = SELECT_EMPL_ROUTE_QUERY % (
            "R_routeID, R_routeName, timeStart, timeEnd", "SCHEDULED", "B_busID", "busID", "BUS", "E_driver = " + ssn);
    elif (choice == "X"):
        EndProgram();
    # No valid input, restart the prompts
    else:
        EmployeeQueries();

    result = SubmitQuery(query);
    if (result is None):
        print("Error Submitting Query.");
        return None;
    # If the result is empty that means the system returned an empty set
    elif (len(result) == 0):
        print("Empty Set: No values exist for request.")
        return True;
    else:
        for line in result:
            print(DisplayClean(line));
        return True;


# Sets a current employee's address. Employee must exist beforehand.
def SetAddress(E_ssn):
    SeparatingLine();
    US_States = set(["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS",
                     "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY",
                     "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV",
                     "WI", "WY"]);
    # Dictionary (map) for employee's address
    empDict = {"Street": "",
               "City": "",
               "State": "",
               "Zip code": ""}
    for key in empDict:
        while (empDict.get(key) == ""):
            print("Please fill out the Employee's address. \n"
                  "Enter 'X' at any time to exit the program.");
            entry = "";
            entry = input("Please enter employee's " + key + ": ").upper();
            entry = entry.strip();
            if (entry.upper() == "X"):
                EndProgram();
            if (entry == ""):
                print(key + " cannot be NULL\n");
            if (key == "Street"):
                street = entry;
            if (key == "City"):
                city = entry;
            if (key == "State"):
                if entry not in US_States:
                    print("Error: Invalid U.S State");
                    entry = "";
                    continue;
                else:
                    state = entry;
            if (key == "Zip code"):
                if (len(entry) == 5):
                    try:
                        int(entry);
                        zip = entry;
                    except ValueError:
                        print("Zip code must be a valid 5-digit number");
                        entry = "";
                        continue;
                else:
                    print(key + " must be a valid 5-digit number");
                    entry = "";
                    continue;
                entry = Sanitize(entry);
            empDict[key] = entry;

    query = ADDRESS_INSERT_UPDATE % (E_ssn, street, city, state, zip, street, city, state, zip);
    result = SubmitInsert(query);
    if (result is False):
        print("Error Submitting Insert.");
        return False;
    print("Employee address Successfully added!");
    return True;


# Creates a new employee and optionally, an address for that employee
def NewEmployee():
    SeparatingLine();
    # Dictionary (map) for employee's information
    empDict = {"Social Security Number": "",
               "First Name": "",
               "Middle Initial": "",
               "Last Name": "",
               "Start Date (YYYY-MM-DD)": "",
               "Supervisor SSN": ""}

    # Iterate over the map and enter values
    for key in empDict:
        # While the inserted value isn't valid keep prompting user
        while (empDict.get(key) == ""):
            print("Please fill out the Employee's information. If the value is NULL please write 'NULL'. \n"
                  "Enter 'X' at any time to exit the program.");
            entry = input("Please enter the new Employee's " + key + " :");
            entry = entry.strip();
            # Exit program
            if (entry.upper() == "X"):
                EndProgram();
            # Ensure the start date follows proper date-time format
            if (key == "Start Date (YYYY-MM-DD)" and entry != ""):
                try:
                    dateObj = datetime.strptime(entry, '%Y-%m-%d').date();
                except ValueError:
                    print("Error: Date must be in YYYY-MM-DD format.");
                    entry = "";
                    continue;
                # Entered start date has to be less than 31 days from today (either past or future)
                if (dateObj > date.today() + timedelta(days=31) or
                        dateObj < date.today() - timedelta(days=31)):
                    print("Date must be within 31 days from today");
                    entry = "";

            # Make sure the SSN and Super-SSN can be integers.
            # If expecting SSN and SuperSSN and not null
            if (key == "Social Security Number" or (key == "Supervisor SSN" and entry.upper() != "NULL")):
                # Make sure SSN is 9 long
                if (len(entry) == 9):
                    # Make sure SSN can be int
                    try:
                        int(entry);
                        if (key == "Social Security Number"):
                            ssn = entry;
                    except ValueError:
                        entry = "";
                    # Supervisor SSN can not be same as Employee SSN
                    if (entry == empDict["Social Security Number"]):
                        print("Supervisor SSN can not be the same as the new Employee's SSN. \n"
                              "If there is no Supervisor please enter: NULL");
                        entry = "";
                else:
                    entry = "";
            # If the middle initial is more than 1 character and it's not NULL
            if (key == "Middle Initial" and len(entry) > 1):
                if (entry.upper() == "NULL"):
                    print("Middle initial null.");
                    entry = "NULL";
                else:
                    print("Middle Initial invalid.");
                    entry = ""
            elif (key == "Middle Initial" and len(entry) > 1):
                print("Middle initial null.");
                entry = "NULL";
            if ((key == "First Name" or key == "Last Name")):
                if (entry.upper() == "NULL" or entry.upper() == "" or len(entry) <= 1):
                    print("Invalid value. Cannot be NULL and more than 1")
                    entry = "";
                    entry = Sanitize(entry);
            empDict[key] = entry;

    # Populate a string with the new query
    newValues = "";
    for key in empDict:
        # If SSN or NULL don't put single quote around it
        if (key == "Social Security Number" or key == "Supervisor SSN" or empDict[key] == "NULL"):
            newValues += empDict[key] + ", ";
        # If it's null don't add to string
        elif (empDict[key] != ""):
            newValues += "'" + empDict[key] + "', ";

    # Remove trailing comma
    if (newValues.endswith(', ')):
        newValues = newValues[:-2];
    # Move all data from map to list in order to insert them into

    query = (NEW_EMPLOYEE_INSERT % (newValues));

    result = SubmitInsert(query);
    # global variable accessible anywhere to get Employee's name
    if (result is False):
        print("Error Submitting Query.");
        return False;
    print("New Employee Successfully added!");
    nextChoice = input("Do you want to add address? (Y/N) ");
    if (nextChoice.upper() == "Y"):
        SetAddress(ssn);
    return True;


# Update an employees address; creates address if it doesn't exist or updates the existing address
def UpdateAddress():
    ssn = "";
    valid = False;
    while (not valid):
        SeparatingLine();
        print("Please enter the Social Security Number (9 digits) of the Employee you want to access. \n"
              "Or enter X to exit the program.");
        ssn = input("Enter SSN: ").strip();

        if (ssn.upper() == "X"):
            EndProgram();
            break;
        elif (len(ssn) != 9):
            print("SSN must be 9 digits long.");
            continue;
        try:
            int(ssn);
            valid = True;
        except ValueError:
            print("SSN must be a number.");
            continue;
    SetAddress(ssn);


# Actions for employees
def EmployeeInterface():
    SeparatingLine();

    selection = "";
    while (selection != "X"):
        SeparatingLine();
        print("Please select from one of the following options: ")
        print("Add a new Employee: N \n"
              "Access an Employee's information: I \n"
              "Check route schedule for a given day: C \n"
              "Update Employee address: A \n"
              "Exit Program: X");
        selection = input("Please enter a command: ")
        selection = selection.upper();
        if (selection == "N"):
            NewEmployee();
        elif (selection == "I"):
            EmployeeQueries();
        elif (selection == "C"):
            CheckSchedule();
        elif (selection == "A"):
            UpdateAddress();
    EndProgram();
