import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.find_element(By.XPATH, '//input[@class="wikipedia-search-input"]').send_keys('Selenium')
driver.find_element(By.XPATH, "//input[@type='submit']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//a[normalize-space()='Selenium']").click()
driver.find_element(By.XPATH, "//a[normalize-space()='Selenium in biology']").click()
driver.find_element(By.XPATH, "//a[normalize-space()='Selenium (software)']").click()
driver.find_element(By.XPATH, "//a[normalize-space()='Selenium disulfide']").click()
multi_windows = driver.window_handles
print(multi_windows)

for id in multi_windows:
    driver.switch_to.window(id)
    print(driver.title)
    driver.close()
time.sleep(4)