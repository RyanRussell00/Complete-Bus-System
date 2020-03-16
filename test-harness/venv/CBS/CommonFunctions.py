import re;


# Closes the program.
def EndProgram():
    SeparatingLine();
    print("Successfully disconnected from database.");
    print("Thank you for using the Complete Bus System. Goodbye!");
    exit(0);


# Regex to clean strings for database
def DatabaseClean(strIn):
    result = re.sub("[^a-zA-Z0-9(),.<>_'\s*=-]*", "", str(strIn));
    result = result.strip();
    return result;


# Regex cleans string for display
def DisplayClean(strIn):
    result = re.sub("[^a-zA-Z0-9(),\s]*", "", str(strIn));
    result = result.strip();
    # remove the weird database/python formatting for dates
    if (" datetimedate" in result):
        result = result.replace(" datetimedate", " ");
    if (" time" in result):
        result = result.replace(" time", " ");
    return result;


# Separating line purely for display purposes
def SeparatingLine():
    print("-------------------------------------------------------------");


# Gets all stops on a bus's route on a given date
# Use Case: I want to know at what time the 535 Lynnwood will be at each of its stops on March 15 2020
# This function is left in this file because it's used by both Employees and Passengers
# ToDo: This entire function once we have finalized the creates.
def CheckSchedule():
    SeparatingLine();

    # Dictionary (map) to receive multiple inputs from user
    reqDict = {"Route Number (3 digits)": "",
               "Route Name": "",
               "Date (YYYY-MM-DD): ": ""
               };
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
