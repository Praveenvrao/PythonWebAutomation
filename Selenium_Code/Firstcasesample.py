from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://admin-demo.nopcommerce.com/login")
driver.find_element(By.CLASS_NAME, "email valid").clear()
driver.find_element(By.CLASS_NAME, "email valid").send_keys("admin@yourstore.com")
driver.find_element(By.ID, "Password").clear()
driver.find_element(By.ID, "Password").send_keys("admin")
driver.find_element(By.CLASS_NAME, "button-1 login-button").click()

act_title = driver.title
exp_title = "Dashboard / nopCommerce administration"

if act_title == exp_title:
    print("Test passed")
else:
    print("Test failed")
