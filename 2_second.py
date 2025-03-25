from operator import truediv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
ser_obj = Service("C:/Users/manikavya.mamidi/PycharmProjects/pythonProject/Driver/chromedriver.exe")
driver = webdriver.Chrome(service = ser_obj)
driver.get("https://genieexports-international.myshopify.com/")

driver.maximize_window()

# Wait for the dropdown to be clickable and click to open it
dropdown = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//div[@class='cvc-switcher-btn__content']"))
)
dropdown.click()

# Wait for the options to be visible and click the desired option
option = WebDriverWait(driver, 3).until(
   # EC.element_to_be_clickable((By.XPATH, "//span[text()='United States']"))
EC.element_to_be_clickable((By.XPATH, "//div[@class='cvc-list-item ']" ))

)
option.click()
assert "United States" in option.text, "United States is not selected"

print("Selected option:", option.text)


time.sleep(3)
