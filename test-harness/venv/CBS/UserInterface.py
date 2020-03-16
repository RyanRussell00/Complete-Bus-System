import re;
from datetime import datetime, timedelta, date;

from Database import StartDBConnection;
from Employee import EmployeeInterface;
from Passenger import PassengerInterface;
from CommonFunctions import *;


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
