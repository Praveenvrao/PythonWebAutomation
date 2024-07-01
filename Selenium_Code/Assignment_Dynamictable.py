import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com")
driver.maximize_window()

driver.find_element(By.XPATH, '//input[@name = "username"]')
time.sleep(5)
driver.find_element(By.XPATH, '//input[@placeholder = "Password"]').send_keys('admin123')
driver.find_element(By.XPATH, '//button[@type = "submit"]').click()
time.sleep(3)
driver.find_element(By.XPATH, '//span[@class= "oxd-text oxd-text--span oxd-main-menu-item--name" and normalize-space() = "Admin"]').click()
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span')
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li/a').click()
time.sleep(4)