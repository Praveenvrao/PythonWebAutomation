import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_login_herokuapp():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.maximize_window()
    print(driver.title)
    make_apnmt = driver.find_element(By.XPATH, "/html/body/header/div/a") #full XPath
    make_apnmt.click()

    username = driver.find_element(By.XPATH, "//input[@id = 'txt-username']") #XPath
    username.click()
    username.send_keys("John Doe")
    password = driver.find_element(By.XPATH, "//input[@id = 'txt-password']")
    password.click()
    password.send_keys("ThisIsNotAPassword")

    login_b = driver.find_element(By.XPATH, "//button[@id = 'btn-login']")
    login_b.click()

    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment", "Error in current url"

    time.sleep(5)
    driver.quit()

