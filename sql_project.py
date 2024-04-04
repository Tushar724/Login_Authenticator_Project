import mysql.connector #mysql library and class is a conector
try:
    mydb = mysql.connector.connect(host="localhost",
                                   user = "root",
                                   password="Openit@123",
                                   auth_plugin="mysql_native_password")
    cursor = mydb.cursor()
    q1 = "show databases"
    cursor.execute(q1)
    db = cursor.fetchall()
    if db:
        for i in db:
            print(i)
    
    
    if mydb.is_connected():
        print("Connceted to the MYSQL database")
except mysql.connector.Error as err:
    print(f"Error {err}")
    
finally:
    if 'mydb' in locals() and mydb.is_connected():
        mydb.close()
        print("Connection Closed")