import re;

from Database import StartDBConnection, CloseConnection, SubmitQuery, SubmitInsert, Sanitize

# ToDo: Separate the ac

# Ending semicolons intentionally left out because the sanitize function removes all semicolons
SELECT_QUERY = "SELECT %s FROM %s WHERE %s"
NEW_EMPLOYEE_QUERY = "INSERT INTO EMPLOYEE (ssn, Fname, Minit, Lname, startDate, supervisor) VALUES (%s, '%s', '%s', '%s','%s', %s)"


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
    if (selection == "I"):
        # ToDo a query that gets all information of the employee including their address
        query = "";
    elif (selection == "B"):
        # ToDo a query that gets all busses that employee is assigned to
        query = "";
    elif (selection == "R"):
        # ToDo gets all routes and times that employee is driving. Maybe a limited time frame?
        query = "";
    elif (selection == "X"):
        EndProgram();

    result = SubmitQuery(query);
    # global variable accessible anywhere to get Employee's name
    if (result is None or len(result) != 1):
        print("Error Submitting Query.");
        return None;
    else:
        for line in result:
            print(line);


def NewEmployee():
    SeparatingLine();
    # ToDo: Queries for adding new employees
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
                  "Enter 'X' at any time to exit the program.")
            entry = input("Please enter the new Employee's " + key + " :");
            entry = entry.strip();
            # Exit program
            if (entry.upper() == "X"):
                EndProgram();
            # Ensure the start date follows proper date-time format
            # ToDo: Find somehow to make sure the date is valid (ie not 100 years in the future)
            if (key == "Start Date (YYYY-MM-DD)"):
                print("datetime: " + entry);
                r = re.compile('[0-9]{4}-[0-9]{2}-[0-9]{2}');
                if r.match(entry) is None:
                    print(entry + "Didn't match datetime");
                    entry = "";
            # Make sure the SSN and Super-SSN can be integers.
            # ToDo: Add case where supervisor's SSN is null
            if (key == "Social Security Number" or key == "Supervisor SSN"):
                if (len(entry) == 9):
                    try:
                        int(entry);
                    except ValueError:
                        entry = "";
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
    query = (NEW_EMPLOYEE_QUERY % (allValues[0], allValues[1], allValues[2], allValues[3], allValues[4], allValues[5]));
    print(query);

    result = SubmitInsert(query);
    # global variable accessible anywhere to get Employee's name
    if (result is False):
        print("Error Submitting Query.");
        return False;
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


def EmployeeInterface():
    # SeparatingLine();
    # global ssn;
    # ssn = "";
    # while (ssn.strip() == ""):
    #     print("Please enter your Social Security Number (9 digits). \n"
    #           "Or enter X to exit the program.");
    #     ssn = input("Enter your SSN: ");
    #
    # result = [];
    # if (len(ssn) == 9):
    #     result = ValidateEmployee(ssn);
    # elif (ssn.upper() == "X"):
    #     EndProgram();
    # else:
    #     print("Incorrect input. Please make sure SSN is 9 digits long.");
    #     EmployeeInterface();
    #
    # global name
    # name = "";
    # if (result is not None):
    #     name = result[0];
    # else:
    #     print("Error getting Employee");
    #     EmployeeInterface();

    EmployeeInterfaceActions();


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
        EmployeeInterface();
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
