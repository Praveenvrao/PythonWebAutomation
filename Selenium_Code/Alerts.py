import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/javascript_alerts')
driver.maximize_window()

driver.find_element(By.XPATH, '//button[@onclick="jsAlert()"]').click()
Jsalert = driver.switch_to.alert
print(Jsalert.text)
time.sleep(4)
Jsalert.accept()

driver.find_element(By.XPATH, '//button[@onclick="jsConfirm()"]').click()
Jsconfirmalert = driver.switch_to.alert
print(Jsconfirmalert.text)
time.sleep(4)
Jsconfirmalert.dismiss()

driver.find_element(By.XPATH, '//button[@onclick="jsPrompt()"]').click()
JsPromptalert = driver.switch_to.alert
print(JsPromptalert.text)
time.sleep(4)
Jsconfirmalert.send_keys("Welcome to the course")
Jsconfirmalert.accept()
#Jsconfirmalert.dismiss()
time.sleep(4)

