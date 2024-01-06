import time

from selenium import webdriver
def test_open_amazon():
    driver = webdriver.Chrome()
    driver.get("https://www.amazon.in/")
    print(driver.title)

def test_open_vwo():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/")
    driver.maximize_window()
    time.sleep(5)
    #driver.quit()
    print(driver.title)