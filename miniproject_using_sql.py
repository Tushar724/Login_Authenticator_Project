
import mysql.connector

def register_user():
    print("### Registration ###")
    username = input("Enter your name ")
    password = input("Enter password ")
    
    try:
        db=mysql.connector.connect(
        host="localhost",
        user = "root",
        database = "tushar",
        password="Openit@123",
        auth_plugin="mysql_native_password"
        )
        cursor = db.cursor()
        cursor.execute("use tushar")
        cursor.execute("create table user4 (username varchar(40), password varchar(40))")
        q1="insert into user4 (username,password) values(%s,%s)"
        cursor.execute(q1,(username,password))
        
        db.commit()
        
        q2="select * from user3"
        cursor.execute(q2)
        if db:
            for i in db:
                print(i)
            
        print('Registration done.........')
    
    except mysql.connector.Error as err:
        print(f"Error {err}")
        
    finally:
        if 'db' in locals() and db.is_connected():
            db.close()
            print("Connection Closed")
            
register_user()