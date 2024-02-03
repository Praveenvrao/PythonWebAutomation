import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Edge()
driver.get("https://www.amazon.in/")
driver.find_element(By.CSS_SELECTOR, "input#twotabsearchtextbox").send_keys("Iphone 13")
driver.maximize_window()
driver.find_element(By.ID, "nav-search-submit-button").click()
driver.find_element(By.XPATH, "//*[@class = 'hm-icon nav-sprite']").click()
#time.sleep(5)
#driver.find_element(By.XPATH, '//*[@id="GLUXProgramSpecificSheetSkipLink"]/a')
#driver.find_element(By.CSS_SELECTOR, 'a[href="/ref=nav_logo"]')
time.sleep(5)

