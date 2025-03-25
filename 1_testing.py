from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
ser_obj = Service("C:/Users/manikavya.mamidi/PycharmProjects/pythonProject/Driver/chromedriver.exe")
driver = webdriver.Chrome(service = ser_obj)
driver.get("https://www.w3schools.com/")
driver.maximize_window()

#click on search box
box = driver.find_element(By.XPATH, "//*[@id='tnb-google-search-input']")
#click function
box.click()
#type data


#click on dropdown
dropdown= driver.find_element(By.ID, '//*[@id="navbtn_certified"]')
dropdown.click()

#-----------------------------------------
driver.get("")
time.sleep(3)




