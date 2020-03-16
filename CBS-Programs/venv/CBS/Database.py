import mysql.connector;
import re;

from CommonFunctions import *;


# Starts connection to the database
def StartDBConnection():
    try:
        global mydb;
        mydb = mysql.connector.connect(
            user='CBSadmin',
            password='adminCBS',
            host='complete-bus-system.cqbrsf1hvrmm.us-west-2.rds.amazonaws.com',
            database='CBS'
        );
        global dbCursor;
        dbCursor = mydb.cursor();
        assert (dbCursor is not None), "FATAL: Database connection is null";
    except mysql.connector.errors.DatabaseError as db:
        print("Error connecting to database. Please View The Error Message and Try Again.");
        print(db);


# Sanitizes inputs to the database to prevent SQL injection
def Sanitize(line):
    if (line.strip() == ""):
        return "";
    line = DatabaseClean(line);
    if (";" in line or "DELETE" in line or "DROP" in line):
        print("Sanitization Warning: Illegal statement found. \n"
              "Line may not contain 'DELETE' or 'DROP' or ';'");
        return "";
    return line.strip();


# Submits a query to the database
def SubmitQuery(query):
    query = Sanitize(query);
    if (query == ""):
        return None;
    result = [];
    dbCursor.execute(query + ";");
    for line in dbCursor:
        result.append(DatabaseClean(line));
    return result;


# Submits an insert or update to the database
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
