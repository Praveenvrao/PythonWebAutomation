import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.XPATH, "//input[@name='username']").send_keys('Admin')
time.sleep(2)
driver.find_element(By.XPATH, '//input[@placeholder = "Password"]').send_keys('admin123')
driver.find_element(By.XPATH, '//button[@type = "submit"]').click()
time.sleep(3)
driver.find_element(By.XPATH, "//span[normalize-space()='Admin']").click()
driver.implicitly_wait(2)
driver.find_element(By.XPATH, "//span[normalize-space()='Job']").click()

Jobtitles = driver.find_element(By.XPATH, "//a[normalize-space()='Job Titles']")

act = ActionChains(driver)

act.move_to_element(Jobtitles).perform()
time.sleep(10)

