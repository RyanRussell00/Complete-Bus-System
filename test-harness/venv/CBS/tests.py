import mysql.connector;
import os;
import fnmatch;
import re;

'''
Tests the database to ensure data exists. Expects the database to be populated with test data first.
'''


# Seperating line purely for display purposes
def SeperatingLine():
    print("-------------------------------------------------------------");


# Regex to get only the string with dashes, periods, and underscores
def clean(strIn):
    result = re.sub("[^a-zA-Z0-9,_'.-]*", "", str(strIn));
    result = result.strip();
    if (result.endswith(',')):
        result = result[:-1];
        # print("removed comma: " + result);
    return result;


def readFromFile(path, commands):
    # open file as read only
    try:
        file = open(path, "r");
    except FileNotFoundError:
        print("Couldn't Locate File: " + path);
        return None;

    currLine = "";
    lines = [];

    for line in file:
        #        print(line);
        # If line isnt empty, or a command add to end of the current command
        if (line.strip()):
            # Replace all new lines with spaces
            if ("\n" in line):
                line = line.replace('\n', ' ');
            # Ignore -- comments
            if ("--" in line):
                head, sep, tail = line.partition('--');
                line = head;
            # Ignore # comments
            if ("#" in line):
                head, sep, tail = line.partition('#');
                line = head;

            currLine += line;
        # If the current line isn't empty
        currLine = currLine.strip();
        if (currLine):
            # if we are reading commands and hit a semicolon add to the total lines
            if (commands is True and ';' in line):
                # print(currLine);
                lines.append(currLine);
                currLine = "";
            elif (commands is False):
                # print(currLine);
                lines.append(currLine);
                currLine = "";

    file.close();
    return lines;


def TablesExist():
    dbCursor.execute("SHOW TABLES");
    # add all tables to set to check if they exist later
    expectedTables = {"BUS", "BUS_STOP", "CARD", "EMPLOYEE", "ADDRESS", "FARE_TIER", "ROUTE", "SCHEDULED", "TAPS",
                      "VISITS"};
    count = 0;

    for line in dbCursor:
        line = '%s' % line;
        if (line not in expectedTables):
            print("Found Unexpected Table: " + str(line));
            SeperatingLine();
            return False;
        count += 1;

    # If the total number of tables expected doesnt meet actual counted
    if (count != len(expectedTables)):
        print("Number of actual tables doesn't meet number of expected tables");
        SeperatingLine();
        return False

    return True;


# Runs all commands and queries from given files and tests for expected outputs
def TestCommands(expectedFile, queriesFile):
    expected = readFromFile(expectedFile, False);
    # expected = readFromFile("../auto-test-files/Employee.Expected", False);

    queries = readFromFile(queriesFile, True);
    # queries = readFromFile("../auto-test-files/Employee.Tests", True);

    if (expected is None or queries is None):
        print("Failed to read expected outputs or queries commands");
        SeperatingLine();
        return False;

    print("Que");
    print(queries);
    print("Ex");
    print(expected);

    # Check if one file is empty and the other isn't
    if ((len(queries) == 0 and len(expected) != 0) or (len(queries) != 0 and len(expected) == 0)):
        print("Error: Either testing file or expected file is empty and the other is not.");
        return False;

    # assert (len(queries) == len(
    #     expected)), "Actual queries and expected outputs do not match. Files: " + queriesFile + " and " + expectedFile;

    # Execute each command in the DB and ensure it matches expected output
    qCount = 0;
    eCount = 0;
    while (qCount < len(queries)):
        # try to execute the command, catch any syntax errors and terminate program
        try:
            dbCursor.execute(queries[qCount]);
        except mysql.connector.ProgrammingError as pe:
            print("MYSQL ERROR EXECUTING: " + queries[qCount]);
            print(pe);
            SeperatingLine();
            return False;

        result = dbCursor.fetchall();
        # If the returned result is empty, but we were expecting a not empty
        if (len(queries) != 0 and len(result) == 0):
            print("ERROR: Query: " + queries[qCount] +
                  " returned an empty set but we were expecting a not empty set.");
            return False;

        for line in result:
            print(line);
            if (eCount >= len(expected)):
                print("Ran out of expected outputs.");
                SeperatingLine();
                return False;

            # Clean lines
            # actual = clean(line);
            # expct = clean(expected[eCount]);
            actual = line;
            expct = expected[eCount];

            # print("Actual: " + actual);
            # print("Expected: " + expct);

            if (actual != expct):
                print("Actual and Expected dont match.");
                print("Actual: " + actual);
                print("Expected: " + expct);
                SeperatingLine();
                return False;

            eCount += 1;

            # assert (str(x) == str(expected[n])), "Expected: " + expected[n] + " \n Actual: " + x;
        qCount += 1;
    return True;


# Imports all the testing files from the given directory.
# Files must end in '.Expected' or '.Tests' and the prefix must be identical for pairs of files.
def RunAllAutoTests(dir):
    # Check tables exist
    if (TablesExist() is False):
        return False;

    files = [];
    # Get all files from the directory
    for file in os.listdir(dir):
        # If files match what we are looking for
        if (fnmatch.fnmatch(file, "*.Expected") or fnmatch.fnmatch(file, "*.Tests")):
            file = file.strip();
            # If file path isn't empty
            if (file):
                # print(file);
                files.append(dir + "/" + file);

    # Ensure that there are an even number of files
    if (len(files) % 2 != 0):
        print("Every test file must have a matching expected file. ");
        print("Ensure the files exist and are named properly.");
        print("Files must end in 'Expected.txt' or 'Tests.txt' and the prefix must be identical.");
        SeperatingLine();
        return False;

    # Sort the files to get the matching prefixes next to each other
    files = sorted(files);

    it = iter(files);
    for f in it:
        n = next(it);
        print("Testing: " + f + " | and | " + n);
        # If any of the tests fail stop the tests
        if (TestCommands(f, n) is False):
            return False;


# This function allows to run tests again without having to restart the entire program.
def RefreshTests():
    refresh = "Y";
    while (refresh.upper() == "Y"):
        refresh = input("Refresh Testing Files? Y/N: ");
        if (RunAllAutoTests("../../auto-test-files")):
            print("Some things went wrong. Please view the error messages above.");
            SeperatingLine();


# Gets the database login information from the user and starts the DB connection
def StartDBConnection():
    user = "";
    password = "";
    host = "";
    databaseName = "";

    print("Welcome to the automated tests for the Complete-Bus-System database. \n");
    print("If you witness the program crash please take a screenshot and contact your system admin. \n");

    print("This version of the tests only work on local MySQL and require you to have the database already created");
    confirm = input("I have the database created on my local MySQL: Y/N: ");
    if (confirm.upper() != 'Y'):
        print("Please create the database on your local MySQL and run the program again.")
        exit(1);

    while (user == ""):
        user = input("Please enter the username to your local MySQL database: ");
        print("You entered: " + user);

    while (password == ""):
        password = input("Please enter the password to your local MySQL database: ");
        print("You entered: " + password);

    while (host == ""):
        host = input("Please enter the host to your local MySQL database (commonly `localhost`): ");
        print("You entered: " + host);

    while (databaseName == ""):
        databaseName = input("Please enter the name of the database you want to use (commonly CBS): ");
        print("You entered: " + databaseName);

    try:
        global mydb;
        mydb = mysql.connector.connect(
            user=user,
            password=password,
            host=host,
            database=databaseName
        );
        global dbCursor;
        dbCursor = mydb.cursor();
    except mysql.connector.errors.DatabaseError as db:
        print("Error connecting to database. Please View The Error Message and Try Again.");
        print(db);
        SeperatingLine();
        # Have user try to login again
        StartDBConnection();

    assert (dbCursor is not None), "auto-tests: Database connection is null";

    RefreshTests();


def main():
    # global mydb;
    # global dbCursor;

    # Connect to the DB
    #
    # mydb = mysql.connector.connect(
    #     user='root',
    #     password='root',
    #     host='localhost',
    #     database='CBS'
    # );
    # # Cursor to run commands on the DB
    # global dbCursor;
    # dbCursor = mydb.cursor();
    #
    # TestCommands("../auto-test-files/Bus.Expected", "../auto-test-files/Bus.Tests");

    StartDBConnection();

    # assert (dbCursor is not None), "auto-tests: Database connection is null";

    # RunAllAutoTests("../auto-test-files");

    # TestCommands("../auto-test-files/EmployeeTests.txt", "../auto-test-files/EmployeeExpected.txt");

    mydb.close();
    print("auto-tests successfully completed.")
    print("Closed auto-tests connection.")


# Execute `main()` function
if __name__ == '__main__':
    main()
