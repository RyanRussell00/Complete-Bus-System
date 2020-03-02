import mysql.connector;
print("mysql-connector Found Successfuly");

mydb = mysql.connector.connect(
  user='root',
    password='root',
    host='localhost',
    database='CBS',
    auth_plugin='mysql_native_password'
);

print(mydb);

mydb.close();