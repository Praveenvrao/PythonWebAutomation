import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://www.google.com/')
driver.back()
driver.get("https://www.amazon.in/")
driver.back()
driver.refresh()
driver.implicitly_wait(3)
driver.forward()
driver.quit()