import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/register?")
driver.maximize_window()

#is_displayed & is_enabled
time.sleep(5)
driver.implicitly_wait(10)
searchbox = driver.find_element(By.XPATH, '//input[@placeholder = "Search store"]')
print("Display status is", searchbox.is_displayed())
print("Enable status is", searchbox.is_enabled())

#is_selected
male_radio = driver.find_element(By.XPATH, '//input[@type="radio" and @id="gender-male"]')
female_radio = driver.find_element(By.XPATH, '//input[@type="radio" and @id="gender-female"]')
print("Male radio button status", male_radio.is_selected())
print("Female radio button status", female_radio.is_selected())

male_radio.click()
print("Male radio button status", male_radio.is_selected())
print("Female radio button status", female_radio.is_selected())

female_radio.click()
print("Male radio button status", male_radio.is_selected())
print("Female radio button status", female_radio.is_selected())

driver.close()
driver.quit()