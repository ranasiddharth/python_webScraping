from selenium import webdriver
driver = webdriver.Chrome(executable_path="D:\chromedriver.exe")
from time import sleep
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://m.facebook.com/anshul.d.sharma.7/about")
print("Opened facebook")
sleep(1)

login_page = driver.find_element_by_xpath('//*[@id="mobile_login_bar"]/div[2]/a[1]')
login_page.click()

usr=input('Enter Email Id:')
pwd=input('Enter Password:')
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

SCROLL_PAUSE_TIME = 2

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