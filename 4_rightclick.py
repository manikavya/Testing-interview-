from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
ser_obj = Service("/Driver/chromedriver.exe")
driver = webdriver.Chrome(service = ser_obj)
driver.get("https://www.w3schools.com/")
driver.maximize_window()

#click on search box
box = driver.find_element(By.XPATH, "//*[@id='tnb-google-search-input']")
actions = ActionChains(driver)
actions.context_click(box).perform()
time.sleep(3)
