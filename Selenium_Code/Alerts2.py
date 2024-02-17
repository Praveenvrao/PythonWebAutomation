import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://mypage.rediff.com/login/dologin")
driver.maximize_window()

driver.find_element(By.XPATH, '//input[@type = "submit"]').click()
time.sleep(4)
driver.switch_to.alert.accept()
driver.switch_to.alert.dismiss()
