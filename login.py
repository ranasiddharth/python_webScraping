from selenium import webdriver
driver = webdriver.Chrome(executable_path="D:\chromedriver.exe")
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://m.facebook.com/")
print("Opened facebook")
sleep(1)

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

pass_box = driver.find_element_by_class_name('_2pii')
pass_box.click()
sleep(1)



print("Done")
input('Press anything to quit')
driver.quit()
print("Finished")