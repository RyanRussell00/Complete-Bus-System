import re;
from datetime import datetime, timedelta, date;

from Database import StartDBConnection;
from Employee import EmployeeInterface;
from Passenger import PassengerInterface;
from FormattingFunctions import *;


# Separating line purely for display purposes
def SeparatingLine():
    print("-------------------------------------------------------------");


# Gets all stops on a busses route on a given date
# Use Case: I want to know at what time the X-Bus will be at each of its stops on March 15 2020
# This function is left in this file because it's used by both Employees and Passengers
# ToDo: This entire function once we have finalized the creates.
# ToDo: Test this function
def CheckSchedule():
    SeparatingLine();
    # ToDo: Queries for getting all stops on a route and what times the bus is supposed to stop at the stops on a day.

    # Dictionary (map) to receive multiple inputs from user
    reqDict = {"Route Number (3 digits)": "",
               "Route Name": "",
               "Date (YYYY-MM-DD): ": ""
               };
    entry;
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
            # Ensure date/time is valid
            if (key == "Start Date (YYYY-MM-DD)"):
                print("datetime: " + entry);
                r = re.compile('[0-9]{4}-[0-9]{2}-[0-9]{2}');
                if r.match(entry) is None:
                    print(entry + "Date must be in format: YYYY-MM-DD");
                    entry = "";
    allValues = [];
    for val in empDict.values():
        allValues.append(val);
    print(allValues);
    if (len(allValues) != 3):
        print("Something went wrong with inputting data.");
        return False;
    # ToDo: Query
    query = "";
    print(query);

    result = SubmitInsert(query);
    # global variable accessible anywhere to get Employee's name
    if (result is False):
        print("Error Submitting Query.");
        return False;
    # If the result is empty that means the system returned an empty set
    elif (len(result) == 0):
        print("Empty Set: No values exist for request.")
    else:
        for line in result:
            print(line);
    return True;


# def EndProgram():
#     SeparatingLine()
#     CloseConnection();
#     print("Successfully disconnected from database.");
#     print("Thank you for using the Complete Bus System. Goodbye!");
#     exit(0);


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
