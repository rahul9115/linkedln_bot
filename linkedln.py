from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
import os

## #### Step 1- Load LinkedIn Homepage ##
#Get the webdriver path
base_path=os.getcwd()
driver = webdriver.Chrome (f"{base_path}/chromedriver.exe")
#Provide the LinkedIn URL that we wish to automatically open
url = 'https://www.linkedin.com/home'
#Open LinkedIn & pause at this step for 3 secs
driver.get(url)
time.sleep (3)

driver.get(url)
time.sleep (3)
##########_ Step 2- Signing In #######
#Get the input field for signing in on LinkedIn home page from the 'inspect' tool
email = driver.find_element_by_xpath("//input[@name ='session_key']")
password = driver.find_element_by_xpath("//input[@name = 'session_password']")

email.send_keys ("swatiaparna2011@gmail.com")
password.send_keys ("swatinla@2478")

driver.find_element_by_xpath("//button[@type ='submit']").click()
search=driver.find_element_by_xpath("//input[@class ='search-global-typeahead__input']")
search.send_keys ("Rahul Vemuri")
search=driver.find_element_by_xpath("//input[@class ='search-global-typeahead__input']")
search.send_keys(Keys.ENTER)
time.sleep (9)
driver.find_element_by_xpath('//a[@class="app-aware-link  artdeco-button artdeco-button--default artdeco-button--2 artdeco-button--muted artdeco-button--secondary"]').click() 

#Read our email & password from separate text files created in Notepad and insert
# with open(r"C:\Users\james\OneDrive\Desktop\username.txt") as myUser:
#     username = myUser.read().replace('\n', '')
#     email.send_keys (username)
# - with open (r"C:\Users\james\OneDrive\Desktop\username.txt") as myPass:
# passcode = myPass.read().replace('\n', '')
# password.send_keys (passcode)
# time.sleep(2)
# #Click the Log in button
# submit= driver.find_element_by_xpath("//button[@type = 'submit']").click()
# time.sleep(2)