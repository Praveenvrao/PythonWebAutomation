import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_login_herokuapp():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.maximize_window()
    print(driver.title)
    make_apnmt = driver.find_element(By.ID, "btn-make-appointment")
    make_apnmt.click()

    username = driver.find_element(By.ID, "txt-username")
    username.click()
    username.send_keys("John Doe")
    password = driver.find_element(By.ID, "txt-password")
    password.click()
    password.send_keys("ThisIsNotAPassword")

    login_b = driver.find_element(By.ID, "btn-login")
    login_b.click()

    time.sleep(10)
    driver.quit()

