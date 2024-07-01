import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
# driver.get("https://www.amazon.in/")
# driver.find_element(By.CSS_SELECTOR, "input#twotabsearchtextbox").send_keys("Iphone 13")
# driver.maximize_window()
# driver.find_element(By.ID, "nav-search-submit-button").click()
# driver.find_element(By.XPATH, "//*[@class = 'hm-icon nav-sprite']").click()
# #time.sleep(5)
# #driver.find_element(By.XPATH, '//*[@id="GLUXProgramSpecificSheetSkipLink"]/a')
# #driver.find_element(By.CSS_SELECTOR, 'a[href="/ref=nav_logo"]')
# time.sleep(5)

# driver.get("https://www.amazon.in/")
# driver.maximize_window()
# driver.find_element(By.ID, "twotabsearchtextbox").send_keys("Dry fruits")
# driver.find_element(By.XPATH, "//input[@id='nav-search-submit-button']").click()
# time.sleep(5)

driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, "input.inputtext").send_keys("abdbdbd")
driver.find_element(By.CSS_SELECTOR, "input.inputtext[data-testid = royal_pass]").send_keys("password")
time.sleep(4)

driver.get("https://www.amazon.in/")
driver.maximize_window()
driver.find_element(By.XPATH, '//input[@name ="field-keywords"]').send_keys("dry fruits")
driver.find_element(By.XPATH, "//input[@id='nav-search-submit-button' and @class ='nav-input nav-progressive-attribute']").click()
time.sleep(5)