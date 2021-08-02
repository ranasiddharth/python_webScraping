import requests
from bs4 import BeautifulSoup
import mysql.connector as c
mydb = c.connect(host="localhost", user="root", password="Kennedy54@$", database="python")

HEADER = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0"
}


def functioncheck(func):
    
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
            print("Record not found in the database")

    return wrapper


@functioncheck
def func(a):
    print(a + " is a pre-existing user")

# func("utkarsh.parkhi.1")


class Person:
    def _init_(self, name, city="Roorkee", work=None):
        if work != None:
            self.work = work
            self.name = name
            self.city = city
        else:
            self.name = name
            self.city = city

    def show(self):
        print(f"My name is {self.name} and my current city is {self.city}")


@functioncheck
def scrap(username):

    url = f"https://www.facebook.com/{username}"
    url2 = f"https://m.facebook.com/{username}/about"
    r = requests.get(url, headers=HEADER)
    r2 = requests.get(url2, headers=HEADER)
    soup = BeautifulSoup(r.content, "html.parser")
    soup2 = BeautifulSoup(r2.content, "html.parser")

    name = soup.find('title').text
    # print(name)

    soup_headers = soup2.find_all('header')
    # print(soup_headers)
    # print(soup2.prettify())

    string1 = "ਕਾਰਜ"
    work_header = ""
    for i in soup_headers:
        if (i.text == string1):
            work_header = i
            break
    # print(work_header)
    work_section = work_header.next_sibling.contents
    # print(work_section)
    work = []
    for item in work_section:
        work.append(list(item.strings)[:])
    # print(work)

    string2 = "ਜਿਨ੍ਹਾਂ ਸਥਾਨਾਂ ਤੋਂ ਲਾਈਵ ਕੀਤਾ ਗਿਆ"
    current_city_header = ""
    for i in soup_headers:
        if (i.text == string2):
            current_city_header = i
            break
    # print(current_city_header)
    city = []
    current_city_section = current_city_header.next_sibling.contents
    # print(current_city_section)
    for item in current_city_section:
        city.append(list(item.strings)[:])
    # print(city)
    current_city = ""
    # print(len(city))
    # print(len(work))
    if len(city)>0 :
        current_city = city[0][0]
        # print(current_city)

scrap("anshul.d.sharma.7")
