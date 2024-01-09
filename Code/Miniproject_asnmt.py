import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.mark.negativelogin
def test_negative_vwo_login():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/")
    print(driver.title)
    mail_ad = driver.find_element(By.XPATH, "//input[@id = 'login-username']")
    mail_ad.click()
    mail_ad.send_keys("adminnnn")
    password = driver.find_element(By.XPATH, "//input[@id = 'login-password']")
    password.click()
    password.send_keys("adminn")
    signin = driver.find_element(By.XPATH, "//span[@data-qa = 'ezazsuguuy']")
    signin.click()
    time.sleep(2)

    error = driver.find_element(By.XPATH, "//div[@id='js-notification-box-msg']")
    assert error.is_displayed(), "Your email, password, IP address or location did not match"
    print(error.is_displayed())
    time.sleep(5)


def test_valid_login():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/")
    print(driver.title)
    email_ad = driver.find_element(By.XPATH, "//input[@id = 'login-username']")
    email_ad.click()
    email_ad.send_keys("contact+atb5x@thetestingacademy.com")
    password = driver.find_element(By.XPATH, "//input[@id = 'login-password']")
    password.click()
    password.send_keys("ATBx@1234")
    sign_in = driver.find_element(By.XPATH, "//button[@id='js-login-btn']")
    sign_in.click()
    time.sleep(3)

    assert driver.current_url == "https://app.vwo.com/#/dashboard"
    print(driver.title)

    #Login_check = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div[1]/p/span[2]")
    #print(Login_check.text)
    #assert Login_check.is_displayed(), "Welcome message not displayed, login unsuccesful"

    time.sleep(5)

