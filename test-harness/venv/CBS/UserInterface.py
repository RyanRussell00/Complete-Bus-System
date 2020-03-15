import re;

from Database import StartDBConnection, CloseConnection, SubmitQuery, SubmitInsert, Sanitize
from datetime import datetime, timedelta, date

# ToDo: Separate the ac

# Ending semicolons intentionally left out because the sanitize function removes all semicolons
SELECT_QUERY = "SELECT %s FROM %s WHERE %s"
SELECT_ALL_QUERY = "SELECT %s FROM %s"
NEW_EMPLOYEE_INSERT = "INSERT INTO EMPLOYEE (ssn, Fname, Minit, Lname, startDate, supervisor) VALUES (%s, '%s', '%s', '%s','%s', %s)"
SELECT_EMPL_ROUTE_QUERY = "SELECT %s FROM %s WHERE %s IN (SELECT %s FROM %s WHERE %s)"
SELECT_EMPL_SCHEDULE = "SELECT %s FROM %s WHERE % (SELECT %s FROM %s WHERE %s)"


# Separating line purely for display purposes
def SeparatingLine():
    print("-------------------------------------------------------------");


def ValidateEmployee():
    ssn = "";
    valid = False;
    while (not valid):
        print("Please enter the Social Security Number (9 digits) of the Employee you want to access. \n"
              "Or enter X to exit the program.");
        ssn = input("Enter SSN: ");

        if (ssn.upper() == "X"):
            EndProgram();
            continue;
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


# ToDo
def EmployeeQueries():
    SeparatingLine();
    emp = ValidateEmployee();
    if (emp is None or len(emp) < 2):
        return False;

    global ssn;
    ssn = emp[0].strip();
    global name;
    name = emp[1].strip();
    if (ssn == "" or name == ""):
        print("Error: SSN or Name is empty.")
        return False;

    SeparatingLine();
    print("Selected Employee: " + name);
    # ToDo: Code the use cases for the Employees
    choice = "";
    while (choice.upper() != "I" or choice.upper() != "B" or choice.upper() != "R" or choice.upper() != "X"):
        print("Get Employee's information: I \n"
              "Get the buses that the Employee is assigned to: B \n"
              "Get the routes and times that the Employee is driving: R \n"
              "End program: X");
        choice = input("Please enter a command: ");

    query = "";
    if (choice == "I"):
        # ToDo: Test the query
        # Join the employee table and the address table to get the full employee's information
        query = (SELECT_QUERY % ("*", "EMPLOYEE AS E, ADDRESS AS A", "E.ssn = " + ssn + " AND A.E_ssn = " + ssn));

        # query = SELECT_ALL_QUERY % ("*", "EMPLOYEE");
        # employeeAddressQuery = "SELECT * FROM EMPLOYEE AS E, ADDRESS AS A WHERE E.ssn = " + ssn + " AND A.E_ssn = " + ssn;
        # addressQuery = SELECT_QUERY % ("*", "ADDRESS", "E_ssn = " + ssn);

    elif (choice == "B"):
        # ToDo: Test the query
        # Gets all busses that the employee is assigned to
        query = SELECT_QUERY % ("busID, busName", "BUS", "E_driver = " + ssn);
    elif (choice == "R"):
        # ToDo: Test the query
        # Gets all routes that the employee is assigned to
        query = SELECT_EMPL_ROUTE_QUERY % (
            "R_routeID, timeStart, timeEnd", "SCHEDULED", "B_busID", "busID", "BUS", "E_driver = " + ssn);
    elif (choice == "X"):
        EndProgram();

    result = SubmitQuery(query);
    if (result is None):
        print("Error Submitting Query.");
        return None;
    # If the result is empty that means the system returned an empty set
    elif (len(result) == 0):
        print("Empty Set: No values exist for request.")
    else:
        for line in result:
            print(line);


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
            nonlocal entry;
            entry = input("Please enter the new Employee's " + key + " :");
            entry = entry.strip();
            # Exit program
            if (entry.upper() == "X"):
                EndProgram();
            # Ensure the start date follows proper date-time format
            # ToDo: Test the date
            if (key == "Start Date (YYYY-MM-DD)"):
                print("datetime: " + entry);
                # r = re.compile('[0-9]{4}-[0-9]{2}-[0-9]{2}');
                # if r.match(entry) is None:
                #     print(entry + "Didn't match datetime");
                #     entry = "";
                try:
                    dateObj = datetime.strptime(entry, '%Y-%m-%d').date();
                except ValueError:
                    print("Error: Date must be in YYYY-MM-DD format.");
                    entry = "";
                    continue;
                # If the entry isn't empty try to
                if (entry != "" and dateObj - date.today() > timedelta(days=31)):
                    print("Date must be no more than 31 days from today");
                    entry = "";

            # Make sure the SSN and Super-SSN can be integers.
            # ToDo: Add case where supervisor's SSN is null (fixed)
            if (key == "Social Security Number" or key == "Supervisor SSN"):
                if (key == "Supervisor SSN" and entry.upper() != "NULL"):
                    try:
                        int(entry);
                        if (len(entry) != 9):
                            entry = "";
                    except ValueError:
                        entry = "";
                else:
                    if (key == "Supervisor SSN"):
                        entry = "NULL";
                    else:
                        entry = "";
            # ToDo: Make sure middle initial is only 1 character
            if (key == "Middle Initial" and len(entry) > 1 and entry != "NULL"):
                entry = ""
            entry = Sanitize(entry);
            empDict[key] = entry;

    allValues = [];
    for val in empDict.values():
        allValues.append(val);
    print(allValues);
    if (len(allValues) != 6):
        print("Something went wrong with the new Employee's data");
        return False;
    query = (NEW_EMPLOYEE_INSERT % (
        allValues[0], allValues[1], allValues[2], allValues[3], allValues[4], allValues[5]));
    print(query);

    result = SubmitInsert(query);
    # global variable accessible anywhere to get Employee's name
    if (result is False):
        print("Error Submitting Query.");
        return False;
    return True;


# Gets all stops on a busses route between a given time
def CheckSchedule():
    SeparatingLine();
    # ToDo: Queries for getting all stops on a route and what times the bus is supposed to stop at the stops between a given time.

    # print("Please fill out the Employee's information.\n"
    #       "Enter 'X' at any time to exit the program.")
    # entry = input("Employee SSN:");
    # entry = entry.strip();
    # if (entry.upper() == "X"):
    #     EndProgram();
    # if (len(entry) == 9):
    #     try:
    #         int(entry);
    #     except ValueError:
    #         entry = "";
    # else:
    #     entry = "";
    query = SELECT_EMPL_SCHEDULE % (
        "timeStart, timeEnd", "SCHEDULED", "B_busID = ", "busID", "BUS", "E_driver = " + entry);
    result = SubmitQuery(query);
    if (result is False):
        print("Error Submitting Querry.");
        return False;
    return True;


def RouteInterface():
    # ToDo: add code for Route interface

    return True;


def EmployeeInterfaceActions():
    SeparatingLine();

    selection = "";
    while (selection != "X"):
        print("Please select from one of the following options: ")
        print("Add a new Employee: N \n"
              "Access an Employee's schedule: S \n"
              "Check a bus's route: C \n"
              "Search route information: R \n"
              "Exit Program: X");
        selection = input("Please enter a command: ")
        selection = selection.upper();
        if (selection == "N"):
            #     ToDo
            NewEmployee();
        elif (selection == "S"):
            # ToDo
            EmployeeQueries();
        elif (selection == "C"):
            # ToDo
            CheckSchedule();
        elif (selection == "R"):
            # ToDo
            RouteInterface();
    EndProgram();


def EndProgram():
    SeparatingLine()
    CloseConnection();
    print("Successfully disconnected from database.");
    print("Thank you for using the Complete Bus System. Goodbye!");
    exit(0);


# Welcomes the user and lets them select their level of access
def WelcomeUser():
    print("Welcome to the Complete Bus System Database!");
    status = "";
    while (status == ""):
        print("I am a Passenger: P")
        print("I am an Employee: E")
        print("Exit Program: X")
        status = input("Please enter (P) (E) (X): ");

    status = status.upper();
    if (status == "P"):
        # ToDo
        PassengerInterface();
    elif (status == "E"):
        EmployeeInterfaceActions();
    elif (status == "X"):
        EndProgram();
    else:
        WelcomeUser();


def main():
    StartDBConnection();
    WelcomeUser();


# Execute `main()` function
if (__name__ == '__main__'):
    main()
