from Database import *;
from CommonFunctions import *;
from datetime import datetime, timedelta, date

# Semicolons intentionally left out
NEW_CARD_QUERY = "insert into CARD (balance, expiry_date, F_fare) values (%s)";
GET_LAST_QUERY = "SELECT LAST_INSERT_ID()";
GET_CARD_QUERY = "SELECT cardNum, balance, expiry_date, F.fareName FROM CARD AS C JOIN FARE_TIER as F ON C.F_fare = F.tier WHERE cardNum = %s";


# Todo: This function lets passengers add more money to their card and renew their card pushing back their expiry date
def GetCardInfo():
    cardNum = "";
    while (cardNum == ""):
        print("Please enter your card num (9 digits). \n"
              "Or enter X to exit the program.");
        cardNum = input("Please select your card number: ");
        cardNum = cardNum.strip();
        if (cardNum.upper() == "X"):
            EndProgram();
        # Ensure card num is valid
        if (len(cardNum) == 9):
            try:
                cardNum = int(cardNum);
            except ValueError:
                print("Please enter a valid card number with 9 digits.")
                cardNum = "";

    query = GET_CARD_QUERY % (cardNum);
    result = SubmitQuery(query);
    if (result is None or len(result) != 1):
        print("Error getting the card number. Make sure you typed the card number correctly.");
        return "";
    # Display card information
    print("Card Number  |  Balance  |  Expiry Date  |  Fare Status")
    for line in result:
        print(DisplayClean(line));
    return cardNum;

# ToDo
def UpdateCard():
    cardNum = GetCardInfo();
    if (cardNum == ""):
        print("Error: Card not found.");
        return False;

    choice = "";
    while (choice == ""):
        print("Reload Card: R \n"
              "Renew Card:  E \n"
              "Exit Program: X");
        choice = input("Please make a selection: ");
        choice = choice.strip().upper();
        if (choice == "X"):
            EndProgram();
        elif (choice == "R"):
            # ToDo: Reload card
            query = "";


def GetFareTier():
    status = "";
    while (status == ""):
        print("I am a ____ \n"
              "Veteran: 1 \n"
              "Disabled: 2 \n"
              "Student: 3 \n"
              "Child: 4 \n"
              "Adult: 5 \n"
              "Senior: 6 \n"
              "Exit Program: X \n")
        status = input("Please select your status: ");
        status = status.strip();
        if (status.upper() == "X"):
            EndProgram();
        # Ensure status is valid
        try:
            status = int(status);
            if (status < 1 or status > 6):
                status = "";
        except ValueError:
            print("Please select your status (1 - 6).")
            status = "";
    # Convert back to string since it was converted to int in the try statement
    return str(status);


def NewPassenger():
    SeparatingLine();
    # Dictionary (map) for employee's information
    passDict = {"Card Balance (Format: $$$$.$$)": "",
                "Expiry Date": "",
                "Status": ""
                }

    # Set expiry date for 2 years from today
    expiry = date.today() + timedelta(weeks=104);
    # print(str(dateObj));
    passDict["Expiry Date"] = str(expiry);

    # Get card balance
    key = "Card Balance (Format: $$$$.$$)";
    while (passDict.get(key) == ""):
        print("Please fill out the Passenger's information. Empty values not allowed. \n"
              "Enter 'X' at any time to exit the program.");
        entry = input("Please enter the new Passenger's " + key + " :");
        entry = entry.strip();
        # Exit program
        if (entry.upper() == "X"):
            EndProgram();
        elif (len(entry) <= 7):
            try:
                float(entry);
            except ValueError:
                print("Please enter a valid balance in the format: $$$$.$$");
                entry = "";
        passDict[key] = entry;

    # Get user status/fare tier
    status = "";
    while (status == ""):
        status = GetFareTier();
    passDict["Status"] = status;

    # Populate a string with the new query
    newValues = "";
    for key in passDict:
        # Add single quote if expiry date and tell user the Expiry Date
        if (key == "Expiry Date"):
            print("Card Expiry Date: " + passDict[key]);
            newValues += "'" + passDict[key] + "', ";
        else:
            newValues += passDict[key] + ", ";

    # Remove trailing comma and space
    if (newValues.endswith(', ')):
        newValues = newValues[:-2];

    query = (NEW_CARD_QUERY % (newValues));
    # print(query);

    result = SubmitInsert(query);
    # global variable accessible anywhere to get Employee's name
    if (result is False):
        print("Error Submitting Query.");
        return False;
    print("New Passenger Successfully added!");
    # Get the new card id
    cardNum = SubmitQuery(GET_LAST_QUERY);
    for line in cardNum:
        print("New Card Number: " + DisplayClean(line));
    return True;


# ToDo: Test
# Actions for employees
def PassengerInterface():
    selection = "";
    while (selection != "X"):
        SeparatingLine();
        print("Please select from one of the following options: ")
        print("Add a new Passenger/Card: N \n"
              "Reload/Renew a Card: R \n"
              "Get Card history and information: H \n"
              "Check route schedule for a given day: C \n"
              "Exit Program: X");
        selection = input("Please enter a command: ")
        selection = selection.upper();
        if (selection == "N"):
            # ToDo: Test
            NewPassenger();
        elif (selection == "R"):
            # ToDo: Create
            UpdateCard();
        elif (selection == "H"):
            # ToDo: Create
            CardQueries();
        elif (selection == "C"):
            # ToDo: Test
            CheckSchedule();
    EndProgram();
