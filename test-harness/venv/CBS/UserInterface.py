from Database import StartDBConnection, CloseConnection, SubmitQuery

# Select query, ending semicolon intentionally left out
SELECT_QUERY = "SELECT %s FROM %s WHERE %s";


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
def GetEmployee():
    SeparatingLine();
    emp = ValidateEmployee();
    if (emp is None or len(emp) < 2):
        return False;

    ssn = emp[0];
    name = emp[1];
    SeparatingLine();
    print("Selected Employee: " + name);
    # ToDo: Code the use cases for the Employees
    choice = "";
    while (choice == ""):
        print("Get Employee's Information: I \n"
              "Get the buses that the Employee is assigned to \n"
              "Get the routes and times that the Employee is driving.")


def EmployeeActions():
    SeparatingLine();

    selection = "";
    while (selection != "X"):
        print("Please select from one of the following options: ")
        print("Add a new Employee: N \n"
              "Search for an Employee's schedule: S \n"
              "Check a bus's route: C \n"
              "Search route information: R \n"
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
