import mysql.connector;
import re;

print("mysql-connector Found Successfuly");


# def getEmployeeAsCommand(Emp):
#     command = str(Emp.ssn + ", " + Emp.Fname + ", " + Emp.Minit + ", " + Emp.Lname + ", " +
#                   Emp.street + ", " + Emp.city + ", " +
#                   Emp.state + ", " + Emp.zip + ", " + Emp.start_date + ", " + Emp.supervisor);
#
#     return command;


# def testGetTables():
#     dbCursor.execute("SHOW TABLES");
#     # add all tables to set to check if they exist later
#     expectedTables = {"BUS", "BUS_STOP", "CARD", "EMPLOYEE", "FARE_TIER", "ROUTE", "SCHEDULED", "TAPS", "VISITS"};
#     count = 0;
#
#     for line in dbCursor:
#         line = '%s' % line;
#         if (line not in expectedTables):
#             print("Found Unexpected Table: " + str(line));
#             return False;
#         count += 1;
#
#     # If the total number of tables expected doesnt meet actual counted
#     if (count != len(expectedTables)):
#         return False
#
#     return True;
#
#
# def testInsertEmployees():
#     Emp = Employee("123456789", "'Alex'", "'A'", "'Walt'", "'3234 Blade Road'",
#                    "'Seattle'", "'WA'", "'98036'", "'2001-05-22'", "NULL");
#
#     command = getEmployeeAsCommand(Emp);
#
#     dbCursor.execute("INSERT INTO EMPLOYEE VALUES(" + command + ")");
#
#     dbCursor.execute("SELECT * FROM EMPLOYEE");
#     printCommand();


# Main
# mydb = mysql.connector.connect(
#     user='ryanruss',
#     password='ryanruss2020',
#     host='complete-bus-system.cqbrsf1hvrmm.us-west-2.rds.amazonaws.com',
#     database='CBS'
# );

def clean(line):
    return '%s' % line;

# Regex to get only the string with dashes, periods, and underscores
def formatString(strIn):
    result = re.sub("[^a-zA-Z0-9,_'.-]*", "", str(strIn));
    return result.strip();


def printResult(format):
    for line in dbCursor:
        if (format):
            print(formatString(line));
        else:
            print(line);


mydb = mysql.connector.connect(
    user='root',
    password='root',
    host='localhost',
    database='CBS'
);
dbCursor = mydb.cursor();

dbCursor.execute("SELECT * FROM BUS;");
result = dbCursor.fetchall();
for x in result:
    # formatString(x);
    print(formatString(x));
    # print(x);
# printResult(False);
# printResult(True);

mydb.close();
