import mysql.connector as c

mydb = c.connect(host = "localhost", user="root", password="Kennedy54@$", database="python")
        
def functionCheck(func):
    
    def wrapper(username):
        mycursor = mydb.cursor()

        sql = "SELECT * FROM user WHERE username = %s"
        adr = (username,)
        
        mycursor.execute(sql, adr)

        myresult = mycursor.fetchall()

        try:
            if username == myresult[0][0]:
                func(username)
        except:
            print("Record not found")

    return wrapper


@functionCheck
def func(a):
    print(a + " is a pre-existing user")


func("utkarsh.parkhi.1")
