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
    if ("datetime.date" in result):
        result = result.replace("datetime.date", " ");
    if (" time" in result):
        result = result.replace(" time", " ");
    if ("datetimetimedelta" in result):
        result = result.replace("datetimetimedelta", "");
    return result;


def DateClean(strIn):
    result = strIn;
    # remove the weird database/python formatting for dates
    if ("datetime.date" in result):
        result = result.replace("datetime.date", "");
    if (" time" in result):
        result = result.replace(" time", " ");
    if ("datetimetimedelta" in result):
        result = result.replace("datetimetimedelta", "");
    result = re.sub("[^a-zA-Z0-9.,\s]*", "", str(result));
    result = result.strip();
    # Replace commas with dashes for date formatting
    result = result.replace(", ", "-");
    result = result.replace(",", "");
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
