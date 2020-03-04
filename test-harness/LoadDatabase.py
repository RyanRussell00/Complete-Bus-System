import mysql.connector;

#Import for testing
from FKTests import testAll

print("mysql-connector Found Successfuly");

def printCommand():
    for line in dbCursor:
        print(line);

# Create Database based on the file-
def createDatabaseFromFile(path):
    # open file as read only
    file = open(path, "r");
    currCommand = "";

    for line in file:
        #        print(line);
        # If line isnt empty add to end of the current command
        if (line.strip()):
            # print("inserting:");
            # print(line);
            currCommand += line;
        # once we hit a semicolon, run all the previous commands
        if (";" in line):
            dbCursor.execute(currCommand);
            currCommand = "";

    file.close();
    print("Finished Creating Database");

def insertFromFile(path):
    # open file as read only
    file = open(path, "r");
    currCommand = "";

    for line in file:
        #        print(line);
        # If line isnt empty, or a command add to end of the current command
        if (line.strip()):
            # Ignore -- comments
            if ("--" in line):
                head, sep, tail = line.partition('--');
                line = head;
            # Ignore # comments
            if ("#" in line):
                head, sep, tail = line.partition('--');
                line = head;
            # Replace all new lines with spaces to prevent SQL errors
            if ("\n" in line):
                line = line.replace('\n', ' ');

            # print("inserting:");
            # print(line);
            currCommand += line;
        # once we hit a semicolon, run all the previous commands
        if (";" in line):
            try:
                # print("Executing command: " + currCommand);
                dbCursor.execute(currCommand);
                currCommand = "";
            except:
                print("FATAL: Failed trying to execute command: " + currCommand);
                file.close();
                return;

    file.close();
    # commit() is needed to update the table
    mydb.commit();
    print("Finished Inserting Into Database");


# --- Start of Main ---
mydb = mysql.connector.connect(
    user='root',
    password='root',
    host='localhost'
    # database='CBS'
);
dbCursor = mydb.cursor();

# Create original DB
createDatabaseFromFile("../Setup/Create-Database-V1.sql");

insertFromFile("../Setup/Inserts_V1.txt");

#Call test from testing file
testAll();

mydb.close();
# --- End of Main ---

#Old Code

# class Employee(object):
#     ssn = "";
#     Fname = "";
#     Minit = "";
#     Lname = "";
#     street = "";
#     city = "";
#     state = "";
#     zip = "";
#     start_date = "";
#     supervisor = "";
#
#     def __init__(self, ssn, Fname, Minit, Lname, street, city, state, zip, start_date, supervisor):
#         self.ssn = ssn;
#         self.Fname = Fname;
#         self.Minit = Minit;
#         self.Lname = Lname;
#         self.street = street;
#         self.city = city;
#         self.state = state;
#         self.zip = zip;
#         self.start_date = start_date;
#         self.supervisor = supervisor;

# def getEmployeeAsCommand(Emp):
#     command = str(Emp.ssn + ", " + Emp.Fname + ", " + Emp.Minit + ", " + Emp.Lname + ", " +
#                   Emp.street + ", " + Emp.city + ", " +
#                   Emp.state + ", " + Emp.zip + ", " + Emp.start_date + ", " + Emp.supervisor);
#
#     return command;