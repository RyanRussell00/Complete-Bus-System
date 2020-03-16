import re;


# Closes the program.
def EndProgram():
    SeparatingLine();
    print("Successfully disconnected from database.");
    print("Thank you for using the Complete Bus System. Goodbye!");
    exit(0);


# Regex to clean strings for database
def DatabaseClean(strIn):
    result = re.sub("[^a-zA-Z0-9(),._'\s*=-]*", "", str(strIn));
    result = result.strip();
    return result;


# Regex cleans string for display
def DisplayClean(strIn):
    result = re.sub("[^a-zA-Z0-9\s]*", "", str(strIn));
    result = result.strip();
    return result;


# Separating line purely for display purposes
def SeparatingLine():
    print("-------------------------------------------------------------");
