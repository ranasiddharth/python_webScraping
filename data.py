import mysql.connector as c
mydb = c.connect(host="localhost", user="root", password="Kennedy54@$", database="python")
import json
class Person:
    def __init__(self, name, city="Roorkee", work=None):
        if work is not None:
            self.work = work
            self.name = name
            self.city = city
        else:
            self.name = name
            self.city = city

    def show(self):
        print(f"My name is {self.name} and my current city is {self.city}")

    def insertdata(self, username):
        mycursor = mydb.cursor()
        mycursor.execute("UPDATE user SET name=%s, city=%s, work=%s WHERE username=%s", (str(self.name), str(self.city), json.dumps(self.work), username))
        mydb.commit()


def existcheck(username):
    mycursor = mydb.cursor()

    sql = "SELECT * FROM user WHERE username = %s"
    adr = (username,)

    mycursor.execute(sql, adr)

    myresult = mycursor.fetchall()
    print(myresult)
    for e in myresult:
        if e[1] is not None:
            if e[2] is not None:
                if e[3] is not None:
                    return Person(name=e[1], city=e[2], work=e[3])
                else:
                    return Person(name=e[1], city=e[2])
            else:
                if e[3] is not None:
                    return Person(name=e[1], work=e[3])
                else:
                    return Person(name=e[1])
        else:
            return None


check = existcheck("utkarsh.parkhi.1")
if check is None:
    print("hello")
else:
    print(check)

