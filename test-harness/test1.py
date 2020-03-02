import mysql.connector;
import re;

print("mysql-connector Found Successfuly");


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


# Regex to get only the string with dashes, periods, and underscores
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

#
# def testInsertEmployees():
#     Emp = Employee("123456789", "Alex", "A", "Walt", "3234 Blade Road",
#                   "Seattle", "WA", "98036", "05-22-2001");
#
#     dbCursor.execute("INSERT INTO TABLE EMPLOYEE VALUES (" + Emp.ssn + Emp.Fname + Emp.Minit + Emp.Lname +
#                      Emp.street + Emp.city + Emp.state + Emp.zip + Emp.start_date + Emp.supervisor);


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

# testInsertEmployees();

mydb.close();
