import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_item_collection():
    driver = webdriver.Chrome()
    driver.get("https://www.ebay.com/")
    driver.maximize_window()
    print(driver.title)

    search_box = driver.find_element(By.XPATH, "//input[@id = 'gh-ac']")
    search_box.click()
    search_box.send_keys("16 gb laptops")
    search_btn = driver.find_element(By.CSS_SELECTOR, "input[id ='gh-btn']")
    search_btn.click()
    time.sleep(3)
    #assert driver.current_url == "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p4432023.m570.l1313&_nkw=16gb+laptops&_sacat=0"
    print(driver.current_url.title())

    driver.quit()