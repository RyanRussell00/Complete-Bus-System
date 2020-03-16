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
    if ("datetimetimedelta" in result):
        result = result.replace("datetimetimedelta", "");
    return result;


# Separating line purely for display purposes
def SeparatingLine():
    print("-------------------------------------------------------------");


def GetDay():
    entry = "";
    while (entry == ""):
        print("Weekday: W");
        print("Weekend: E");
        print("Holiday: H");
        print("Snow: S");
        print("Exit Program: X");
        entry = input("Enter your selection: ").strip().upper();
        if (entry == "X"):
            EndProgram();
        if (entry == "W"):
            return "Weekday";
        if (entry == "E"):
            return "Weekend";
        if (entry == "H"):
            return "Holiday";
        if (entry == "S"):
            return "Snow";
        else:
            entry = "";
            continue;
