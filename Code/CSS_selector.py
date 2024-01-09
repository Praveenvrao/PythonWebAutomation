import time
from  selenium import webdriver
from selenium.webdriver.common.by import By

def test_open_url():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    print(driver.title)
    assert driver.title == "CURA Healthcare Service"
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/"

    time.sleep(3)
    make_apnt_btn = driver.find_element(By.CSS_SELECTOR, "a[id ='btn-make-appointment']")
    make_apnt_btn.click()
    time.sleep(2)
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"

    username = driver.find_element(By.CSS_SELECTOR, "input[id = 'txt-username']")  # XPath
    username.click()
    username.send_keys("John Doe")
    password = driver.find_element(By.CSS_SELECTOR, "input[id = 'txt-password']")
    password.click()
    password.send_keys("ThisIsNotAPassword")

    login_b = driver.find_element(By.XPATH, "//button[@id = 'btn-login']")
    login_b.click()
