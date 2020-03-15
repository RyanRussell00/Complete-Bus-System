import mysql.connector;
import re;

from FormattingFunctions import *;


def StartDBConnection():
    user = "root";
    password = "root";
    host = "localhost";
    databaseName = "CBS";

    while (user == ""):
        user = input("Please enter the username to the database: ");
        print("You entered: " + user);

    while (password == ""):
        password = input("Please enter the password to the database: ");
        print("You entered: " + password);

    while (host == ""):
        host = input("Please enter the host to the database: ");
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
        assert (dbCursor is not None), "FATAL: Database connection is null";
    except mysql.connector.errors.DatabaseError as db:
        print("Error connecting to database. Please View The Error Message and Try Again.");
        print(db);


# # Closes the connection to the database, if its not connected just ignore it
# def CloseConnection():
#     try:
#         mydb.close();
#     except NameError:
#         return;


# Gets the cursor to the database, if it hasn't been created yet gives a None value
def GetDBCursor():
    try:
        return dbCursor;
    except NameError:
        return None;


def Sanitize(line):
    if (line.strip() == ""):
        return "";
    line = DatabaseClean(line);
    # print("DatabaseCleaned: " + line);
    if (";" in line or "DELETE" in line or "DROP" in line):
        print("Sanitization Warning: Illegal statement found. \n"
              "Line may not contain 'DELETE' or 'DROP' or ';'");
        return "";
    # print("Sanitized: " + line.strip());
    return line.strip();


def SubmitQuery(query):
    query = Sanitize(query);
    if (query == ""):
        return None;
    result = [];
    dbCursor.execute(query + ";");
    for line in dbCursor:
        result.append(DatabaseClean(line));
    return result;


def SubmitInsert(insert):
    insert = Sanitize(insert);
    if (insert == ""):
        return False;
    print("Inserting:");
    print(insert);
    try:
        dbCursor.execute(insert + ";");
        mydb.commit();
    except Exception as e:
        print("Failed trying to insert, see error message:");
        print(e);
        return False;

    return True;

#
# def ConnectDatabase():
#     # Remote Database currently unavailable, rereouting to local database
#     print("Remote Database currently unavailable, connect to local database instead");
#     StartDBConnection(False);


# def ConnectLocalDatabase(user, password, host, databaseName):
#     try:
#         mydb = mysql.connector.connect(
#             user=user,
#             password=password,
#             host=host,
#             database=databaseName
#         );
#         dbCursor = mydb.cursor();
#         assert (dbCursor is not None), "FATAL: Database connection is null";
#         return True;
#     except mysql.connector.errors.DatabaseError as db:
#         print("Error connecting to database. Please View The Error Message and Try Again.");
#         print(db);
#         return False;
#


# if (remote):
#     if (ConnectRemoteDatabase(user, password, host, databaseName)):
#         LaunchUserInterface();
# else:
#     if (ConnectLocalDatabase(user, password, host, databaseName)):
#         LaunchUserInterface();


#
#
# # Gets the database login information from the user and starts the DB connection
# def SelectDB():
#     dbType = "";
#
#     while (dbType.strip() == ""):
#         dbType = input('To connect to local MySQL enter "M" | To connect to AWS database enter "A": ');
#
#     dbType = dbType.upper();
#     if (dbType == "M"):
#         StartDBConnection(False);
#     elif (dbType == "A"):
#         StartDBConnection(True);
#     else:
#         SelectDB();
