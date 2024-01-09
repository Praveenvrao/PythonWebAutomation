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

    #make_apnt_btn = driver.find_element(By.XPATH, "//a[@id ='btn-make-appointment']")
    #make_apnt_btn_text = driver.find_element(By.XPATH, "//a[text()='Make Appointment']")
    make_apnt_btn_contains = driver.find_element(By.XPATH, "//a[contains(text(),'Make Appointment')]")
    make_apnt_btn_contains.click()
    #make_apnt_btn_text.click()
    #make_apnt_btn.click()

    time.sleep(3)
    

    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"