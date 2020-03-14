# from tests import *
# from ConnectDatabase import *
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
#
#
# def main():
#     SelectDB();
#
#
# # Execute `main()` function
# if (__name__ == '__main__'):
#     main()
