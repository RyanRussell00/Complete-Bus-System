import mysql.connector;


def testGetTables():
    dbCursor.execute("SHOW TABLES");
    # add all tables to set to check if they exist later
    expectedTables = {"BUS", "BUS_STOP", "CARD", "EMPLOYEE", "FARE_TIER", "ROUTE", "SCHEDULED", "TAPS", "VISITS"};
    count = 0;

    for line in dbCursor:
        line = '%s' % line;
        # Testing
        print(line);
        if (line not in expectedTables):
            print("Found Unexpected Table: " + str(line));
            return False;
        count += 1;

    # If the total number of tables expected doesnt meet actual counted
    if (count != len(expectedTables)):
        print("FATAL: EXPECTED TABLES DO NOT EXIST");
        quit();

    print("Tables Exist");


def test1():
    print("Test 1");


def test2():
    print("Test 2");


def test3():
    print("Test 3");


def test4():
    print("Test 4");


def test5():
    print("Test 5");


def test6():
    print("Test 6");


def test7():
    print("Test 7");


def test8():
    print("Test 8");


# Calls all the testing functions
def testAll():
    testGetTables();
    test1();
    test2();
    test3();
    test4();
    test5();
    test6();
    test7();
    test8();


# --- Start of Main ---
# --- Start of Main ---
mydb = mysql.connector.connect(
    user='root',
    password='root',
    host='localhost',
    database='CBS'
);
dbCursor = mydb.cursor();
# --- End of Main ---
