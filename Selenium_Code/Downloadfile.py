import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://cgi-lib.berkeley.edu/ex/fup.html")
driver.maximize_window()
driver.find_element(By.XPATH, "//input[@name = 'upfile']").click()
time.sleep(7)