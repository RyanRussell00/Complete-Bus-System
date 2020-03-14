import mysql.connector;
import os;
import fnmatch;

'''
Tests the database to ensure data exists. Expects the database to be populated with test data first.
'''


# Cleans the output of the database. Does not convert it to string.
# Example: (111222333,) becomes: 111222333
def clean(line):
    return '%s' % line;


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


# Runs all commands and queries from given files and tests for expected outputs
def TestCommands(expectedFile, queriesFile):
    expected = readFromFile(expectedFile, False);
    assert (expected is not None);

    queries = readFromFile(queriesFile, True);
    assert (queries is not None);

    # print(queries);
    # print(expected);

    assert (len(queries) == len(
        expected)), "Actual queries and expected outputs do not match. Files: " + queriesFile + " and " + expectedFile;

    # Execute each command in the DB and ensure it matches expected output
    n = 0;
    while (n < len(queries)):
        # try to execute the command, catch any syntax errors and terminate program
        try:
            dbCursor.execute(queries[n]);
        except mysql.connector.ProgrammingError as pe:
            print("MYSQL ERROR EXECUTING: " + queries[n]);
            print(pe);
            print("Terminating Tests.");
            exit(1);
        for x in dbCursor:
            x = clean(x);
            assert (str(x) == str(expected[n])), "Expected: " + expected[n] + " \n Actual: " + x;
        n += 1;


# Imports all the testing files from the given directory.
# Files must end in 'Expected.txt' or 'Tests.txt' and the prefix must be identical.
def RunAllAutoTests(dir):
    files = [];
    # Get all files from the directory
    for file in os.listdir(dir):
        # If files match what we are looking for
        if (fnmatch.fnmatch(file, "*Expected.txt") or fnmatch.fnmatch(file, "*Tests.txt")):
            file = file.strip();
            # If file path isn't empty
            if (file):
                # print(file);
                files.append(dir + "/" + file);

    # Ensure that there are an even number of files
    assert (len(
        files) % 2 == 0), "Every test file must have a matching expected file. " + "Ensure the files exist and are named properly. \n "
    "Files must end in 'Expected.txt' or 'Tests.txt' and the prefix must be identical."

    # Sort the files to get the matching prefixes next to each other
    files = sorted(files);

    it = iter(files);
    for f in it:
        n = next(it);
        print("Testing: " + f + " | and | " + n);
        TestCommands(f, n);


def main():
    # Connect to the DB
    mydb = mysql.connector.connect(
        user='root',
        password='root',
        host='localhost',
        database='CBS'
    );
    # Cursor to run commands on the DB
    global dbCursor;
    dbCursor = mydb.cursor();
    assert (dbCursor is not None), "auto-tests: Database connection is null";

    RunAllAutoTests("../auto-test-files");

    # TestCommands("../auto-test-files/EmployeeTests.txt", "../auto-test-files/EmployeeExpected.txt");

    mydb.close();
    print("auto-tests successfully completed.")
    print("Closed auto-tests connection.")


# Execute `main()` function
if __name__ == '__main__':
    main()
