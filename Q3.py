import requests
from bs4 import BeautifulSoup
from selenium import webdriver
driver = webdriver.Chrome(executable_path="D:\chromedriver.exe")
from time import sleep
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

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


def func_work(username, soup2):
    soup_headers = soup2.find_all('header')
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
    return work

def func_name(username, soup):
    name = soup.find('title').text
    # print(name)
    return name

def func_city(username, soup2):
    soup_headers = soup2.find_all('header')
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
    if len(city) > 0:
        current_city = city[0][0]
        # print(current_city)

def func_fav(username):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://m.facebook.com/anshul.d.sharma.7/about")
    print("Opened facebook")
    sleep(1)

    login_page = driver.find_element_by_xpath('//*[@id="mobile_login_bar"]/div[2]/a[1]')
    login_page.click()

    usr = input('Enter Email Id:')
    pwd = input('Enter Password:')
    username_box = driver.find_element_by_id('m_login_email')
    username_box.send_keys(usr)
    print("Email Id entered")
    sleep(1)

    password_box = driver.find_element_by_id('m_login_password')
    password_box.send_keys(pwd)
    print("Password entered")

    # finding login_button using div id
    login_box = driver.find_element_by_id('login_password_step_element')
    login_box.click()
    sleep(1)

    SCROLL_PAUSE_TIME = 10

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    time.sleep(2)

    likes_list = driver.find_elements(By.XPATH, '/html/body/div[1]/div[1]/div[4]/div/div[1]/div/div[2]/div[11]/div/div/div/div/div/div/div/div[*]/div/span')
    fav = []
    # print(likes_list)
    for elem in likes_list:
        fav.append(elem.text)
    print("Favourites of this user are: ")
    print(fav)

    # print("Done")
    # input('Press anything to quit')
    driver.quit()
    # print("Finished")


@functioncheck
def scrap(username):

    url = f"https://www.facebook.com/{username}"
    url2 = f"https://m.facebook.com/{username}/about"
    r = requests.get(url, headers=HEADER)
    r2 = requests.get(url2, headers=HEADER)
    soup = BeautifulSoup(r.content, "html.parser")
    soup2 = BeautifulSoup(r2.content, "html.parser")

    name = func_name(username, soup)
    work = func_work(username, soup2)
    city = func_city(username, soup2)
    func_fav(username)

    # name = soup.find('title').text
    # print(name)

    # soup_headers = soup2.find_all('header')
    # print(soup_headers)
    # print(soup2.prettify())

    # string1 = "ਕਾਰਜ"
    # work_header = ""
    # for i in soup_headers:
    #     if (i.text == string1):
    #         work_header = i
    #         break
    # # print(work_header)
    # work_section = work_header.next_sibling.contents
    # # print(work_section)
    # work = []
    # for item in work_section:
    #     work.append(list(item.strings)[:])
    # # print(work)

    # string2 = "ਜਿਨ੍ਹਾਂ ਸਥਾਨਾਂ ਤੋਂ ਲਾਈਵ ਕੀਤਾ ਗਿਆ"
    # current_city_header = ""
    # for i in soup_headers:
    #     if (i.text == string2):
    #         current_city_header = i
    #         break
    # # print(current_city_header)
    # city = []
    # current_city_section = current_city_header.next_sibling.contents
    # # print(current_city_section)
    # for item in current_city_section:
    #     city.append(list(item.strings)[:])
    # # print(city)
    # current_city = ""
    # # print(len(city))
    # # print(len(work))
    # if len(city)>0 :
    #     current_city = city[0][0]
    #     # print(current_city)

scrap("anshul.d.sharma.7")
