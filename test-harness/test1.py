import mysql.connector;
import re;

print("mysql-connector Found Successfuly");


#Regex to get only the string with dashes, periods, and underscores
def formatString(strIn):
  result = re.sub("[^a-zA-Z0-9_.-]*", "", str(strIn));
  return result;

def testGetTables():
    dbCursor.execute("SHOW TABLES");
    # add all tables to set to check if they exist later
    expectedTables = {"BUS", "BUS_STOP", "CARD", "EMPLOYEE", "FARE_TIER", "ROUTE", "SCHEDULED", "TAPS", "VISITS"};
    count = 0;

    for line in dbCursor:
        result = formatString(line);
        print(result);
        if (result not in expectedTables):
            print("Found Unexpected Table: " + str(line));
            return False;
        count += 1;

    # If the total number of tables expected doesnt meet actual counted
    if (count != len(expectedTables)):
        return False

    return True;

def testInsert():
  dbCursor.execute()


# Main
mydb = mysql.connector.connect(
    user='root',
    password='root',
    host='localhost',
    database='CBS'
);
dbCursor = mydb.cursor();

# Regex to ignore all non-alphabet characters

print("Tables Exist: " + str(testGetTables()));

mydb.close();
