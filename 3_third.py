from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys
ser_obj = Service("C:/Users/manikavya.mamidi/PycharmProjects/pythonProject/Driver/chromedriver.exe")
driver = webdriver.Chrome(service = ser_obj)
driver.get("https://genieexports-international.myshopify.com/")
#driver.get("https://www.orangehrm.com/")
driver.maximize_window()
#driver.find_element(By.LINK_TEXT, "Catalog").click()
driver.find_element(By.XPATH,"//div[@class='cvc-switcher-btn__content']").click()



time.sleep(10)
