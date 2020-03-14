from Database import StartDBConnection, CloseConnection, SubmitQuery

# Select query, ending semicolon intentionally left out
SELECT_QUERY = "SELECT %s FROM %s WHERE %s";


# Separating line purely for display purposes
def SeparatingLine():
    print("-------------------------------------------------------------");


def ValidateEmployee(ssn):
    if (len(ssn) != 9):
        return None;
    query = (SELECT_QUERY % ("Fname, Lname", "EMPLOYEE", "ssn = " + ssn));
    result = SubmitQuery(query);
    if (len(result) != 1):
        print("Could not locate employee with given SSN");
        return None;
    return result;


# ToDo
def GetEmployee():
    print("ToDo: GetEmployee()");


def EmployeeActions():
    SeparatingLine();
    print("Hello, " + name);

    selection = "";
    while (selection == ""):
        print("Please select from one of the following options: ")
        print("Add a new Employee: N \n"
              "Search for an Employee by SSN: S \n"
              "Check your bus schedule: C \n"
              "Search up route information: R \n"
              "Exit Program: X");
        selection = input("Please enter what you'd like to do: ")
    selection = selection.upper();
    if (selection == "N"):
        #     ToDo
        NewEmployee();
    elif (selection == "S"):
        # ToDo
        GetEmployee();
    elif (selection == "C"):
        # ToDo
        CheckSchedule();
    elif (selection == "R"):
        # ToDo
        RouteInterface();
    elif (selection == "X"):
        EndProgram();


def EmployeeInterface():
    SeparatingLine();
    global ssn;
    ssn = "";
    while (ssn.strip() == ""):
        print("Please enter your Social Security Number (9 digits).");
        ssn = input("Enter your SSN: ");

    result = [];
    if (len(ssn) == 9):
        result = ValidateEmployee(ssn);
    else:
        print("Incorrect input. Please make sure SSN is 9 digits long.");
        EmployeeInterface();

    global name
    name = "";
    if (result is not None):
        name = result[0];
    else:
        print("Error getting Employee");
        EmployeeInterface();

    EmployeeActions();


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
