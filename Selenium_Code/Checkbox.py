import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# 1 Selecting oneday
sunday = driver.find_element(By.XPATH, "//input[@type='checkbox' and contains(@id, 'sunday')]")
sunday.click()
driver.implicitly_wait(5)
print(sunday.get_attribute("id"))

driver.quit()