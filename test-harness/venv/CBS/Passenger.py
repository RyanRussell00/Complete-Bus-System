from Database import *;
from FormattingFunctions import *;


# ToDo: Test
# Actions for employees
def PassengerInterface():
    SeparatingLine();

    selection = "";
    while (selection != "X"):
        print("Please select from one of the following options: ")
        print("Add a new Employee: N \n"
              "Access an Employee's schedule: S \n"
              "Check route schedule for a given day: C \n"
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
    EndProgram();
